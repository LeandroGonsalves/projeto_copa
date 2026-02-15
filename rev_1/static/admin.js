document.addEventListener("DOMContentLoaded", function () {

    const grupoSelect = document.getElementById("grupo");
    const partidaSelect = document.getElementById("id_partida");
    const time1Select = document.getElementById("time1");
    const time2Select = document.getElementById("time2");
    const form = document.getElementById("placarForm");
    const btnClassificacao = document.getElementById("btnClassificacao");

    // ================================
    // Carregar grupo ao mudar seleção
    // ================================
    grupoSelect.addEventListener("change", carregarGrupo);

    function carregarGrupo() {
        const grupo = grupoSelect.value;

        fetch("/api/grupo/" + grupo)
            .then(res => res.json())
            .then(data => {

                partidaSelect.innerHTML = "";
                time1Select.innerHTML = "";
                time2Select.innerHTML = "";

                // Carregar partidas
                data.partidas.forEach(p => {
                    const option = document.createElement("option");
                    option.value = p.id_partida;
                    option.textContent =
                        `Partida ${p.id_partida} - ${p.time1} x ${p.time2}`;
                    partidaSelect.appendChild(option);
                });

                // Disparar preenchimento automático
                atualizarTimesDaPartida();
            });
    }

    // ======================================
    // Atualizar automaticamente time1/time2
    // ======================================
    partidaSelect.addEventListener("change", atualizarTimesDaPartida);

    function atualizarTimesDaPartida() {
        const grupo = grupoSelect.value;
        const idPartida = parseInt(partidaSelect.value);

        fetch("/api/grupo/" + grupo)
            .then(res => res.json())
            .then(data => {

                const partida = data.partidas.find(
                    p => p.id_partida === idPartida
                );

                if (partida) {
                    time1Select.innerHTML =
                        `<option value="${partida.time1}">${partida.time1}</option>`;
                    time2Select.innerHTML =
                        `<option value="${partida.time2}">${partida.time2}</option>`;
                }
            });
    }

    // ==========================
    // Enviar atualização placar
    // ==========================
    form.addEventListener("submit", function (e) {
        e.preventDefault();

        fetch("/api/placar", {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                grupo: grupoSelect.value,
                id_partida: parseInt(partidaSelect.value),
                placar: {
                    [time1Select.value]:
                        parseInt(document.getElementById("gols1").value),
                    [time2Select.value]:
                        parseInt(document.getElementById("gols2").value)
                }
            })
        })
            .then(res => res.json())
            .then(data => {
                alert(data.mensagem || data.erro);
            });
    });

    // ======================
    // Carregar Classificação
    // ======================
    btnClassificacao.addEventListener("click", function () {

        fetch("/api/classificacao")
            .then(res => res.json())
            .then(data => {

                const grupoSelecionado =
                    document.getElementById("grupoClassificacao").value;

                const grupo = data[grupoSelecionado];

                if (!grupo) {
                    document.getElementById("tabelaClassificacao").innerHTML =
                        "<p>Sem dados para este grupo.</p>";
                    return;
                }

                let tabela = `
                    <table>
                        <tr>
                            <th>Seleção</th>
                            <th>Pontos</th>
                            <th>GM</th>
                            <th>GS</th>
                            <th>Saldo</th>
                        </tr>
                `;

                grupo.forEach(time => {
                    tabela += `
                        <tr>
                            <td>${time.selecao}</td>
                            <td>${time.pontos}</td>
                            <td>${time.gm}</td>
                            <td>${time.gs}</td>
                            <td>${time.saldo}</td>
                        </tr>
                    `;
                });

                tabela += "</table>";

                document.getElementById("tabelaClassificacao").innerHTML = tabela;
            });
    });

    // Carregar automaticamente ao abrir
    carregarGrupo();

});
