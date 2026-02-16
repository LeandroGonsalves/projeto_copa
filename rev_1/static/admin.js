document.addEventListener("DOMContentLoaded", function () {

    const rodadaSelect = document.getElementById("rodada");
    const grupoSelect = document.getElementById("grupo");
    const partidaSelect = document.getElementById("id_partida");
    const time1Select = document.getElementById("time1");
    const time2Select = document.getElementById("time2");
    const form = document.getElementById("placarForm");
    const btnClassificacao = document.getElementById("btnClassificacao");

    let partidasDoGrupo = [];

    // ======================================
    // CARREGAR GRUPO
    // ======================================
    grupoSelect.addEventListener("change", carregarGrupo);

    function carregarGrupo() {
        const grupo = grupoSelect.value;

        if (!grupo) return;

        fetch("/api/grupo/" + grupo)
            .then(res => res.json())
            .then(data => {
                partidasDoGrupo = data.partidas || [];
                carregarPartidasPorRodada();
            });
    }

    // ======================================
    // CARREGAR PARTIDAS POR RODADA
    // ======================================
    rodadaSelect.addEventListener("change", carregarPartidasPorRodada);

    function carregarPartidasPorRodada() {

        const rodada = parseInt(rodadaSelect.value);

        partidaSelect.innerHTML = "";
        time1Select.innerHTML = "";
        time2Select.innerHTML = "";

        if (!rodada || partidasDoGrupo.length === 0) return;

        const partidasFiltradas = partidasDoGrupo.filter(
            p => p.rodada === rodada
        );

        partidasFiltradas.forEach(p => {
            const option = document.createElement("option");
            option.value = p.id_partida;
            option.textContent =
                `Partida ${p.id_partida} - ${p.time1} x ${p.time2}`;
            partidaSelect.appendChild(option);
        });

        atualizarTimesDaPartida();
    }

    // ======================================
    // ATUALIZAR TIMES AUTOMATICAMENTE
    // ======================================
    partidaSelect.addEventListener("change", atualizarTimesDaPartida);

    function atualizarTimesDaPartida() {

        const idPartida = parseInt(partidaSelect.value);

        if (!idPartida) return;

        const partida = partidasDoGrupo.find(
            p => p.id_partida === idPartida
        );

        if (!partida) return;

        time1Select.innerHTML =
            `<option value="${partida.time1}">${partida.time1}</option>`;

        time2Select.innerHTML =
            `<option value="${partida.time2}">${partida.time2}</option>`;
    }

    // ======================================
    // ENVIAR PLACAR
    // ======================================
    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const gols1 = parseInt(document.getElementById("gols1").value);
        const gols2 = parseInt(document.getElementById("gols2").value);

        // 🔒 Validação extra de segurança
        if (gols1 < 0 || gols2 < 0 || isNaN(gols1) || isNaN(gols2)) {
            alert("Os gols devem ser números inteiros não negativos.");
            return;
        }

        fetch("/api/placar", {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                grupo: grupoSelect.value,
                id_partida: parseInt(partidaSelect.value),
                placar: {
                    [time1Select.value]: gols1,
                    [time2Select.value]: gols2
                }
            })
        })
            .then(res => res.json())
            .then(data => {
                alert(data.mensagem || data.erro);
            });
    });

    // ======================================
    // CLASSIFICAÇÃO
    // ======================================
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

    // ======================================
    // INICIALIZAÇÃO
    // ======================================
    carregarGrupo();

});
