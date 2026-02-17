document.addEventListener("DOMContentLoaded", function () {

    // ===============================
    // ELEMENTOS
    // ===============================

    const rodadaSelect = document.getElementById("rodada");
    const grupoSelect = document.getElementById("grupo");
    const partidaSelect = document.getElementById("id_partida");
    const time1Select = document.getElementById("time1");
    const time2Select = document.getElementById("time2");
    const form = document.getElementById("placarForm");
    const btnClassificacao = document.getElementById("btnClassificacao");

    const selectOitava = document.getElementById("selectOitava");
    const btnAtualizarOitava = document.getElementById("btnAtualizarOitava");

    let partidasDoGrupo = [];

    // ======================================
    // CARREGAR GRUPO
    // ======================================

    function carregarGrupo() {

        if (!grupoSelect) return;

        const grupo = grupoSelect.value;
        if (!grupo) return;

        fetch("/api/grupo/" + grupo)
            .then(res => res.json())
            .then(data => {
                partidasDoGrupo = data.partidas || [];
                carregarPartidasPorRodada();
            })
            .catch(error => console.error("Erro ao carregar grupo:", error));
    }

    if (grupoSelect) {
        grupoSelect.addEventListener("change", carregarGrupo);
    }

    // ======================================
    // CARREGAR PARTIDAS POR RODADA
    // ======================================

    function carregarPartidasPorRodada() {

        if (!rodadaSelect || !partidaSelect) return;

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

    if (rodadaSelect) {
        rodadaSelect.addEventListener("change", carregarPartidasPorRodada);
    }

    // ======================================
    // ATUALIZAR TIMES AUTOMATICAMENTE
    // ======================================

    function atualizarTimesDaPartida() {

        if (!partidaSelect) return;

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

    if (partidaSelect) {
        partidaSelect.addEventListener("change", atualizarTimesDaPartida);
    }

    // ======================================
    // ENVIAR PLACAR (FASE DE GRUPOS)
    // ======================================

    if (form) {
        form.addEventListener("submit", function (e) {

            e.preventDefault();

            const gols1 = parseInt(document.getElementById("gols1").value);
            const gols2 = parseInt(document.getElementById("gols2").value);

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
            })
            .catch(error => console.error("Erro ao atualizar placar:", error));
        });
    }

    // ======================================
    // CLASSIFICAÇÃO
    // ======================================

    if (btnClassificacao) {
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
                })
                .catch(error => console.error("Erro ao carregar classificação:", error));
        });
    }

    // ======================================
    // CARREGAR OITAVAS
    // ======================================

    function carregarOitavas() {

        if (!selectOitava) return;

        fetch("/api/oitavas")
            .then(res => res.json())
            .then(jogos => {

                selectOitava.innerHTML = "";

                if (!jogos || jogos.length === 0) {
                    const option = document.createElement("option");
                    option.textContent = "Nenhuma oitava disponível";
                    selectOitava.appendChild(option);
                    return;
                }

                jogos.forEach(jogo => {
                    const option = document.createElement("option");
                    option.value = jogo.id_jogo;
                    option.textContent =
                        `Jogo ${jogo.id_jogo} - ${jogo.mandante} x ${jogo.visitante}`;
                    selectOitava.appendChild(option);
                });
            })
            .catch(error => console.error("Erro ao carregar oitavas:", error));
    }

    // ======================================
    // ATUALIZAR PLACAR OITAVAS
    // ======================================

    if (btnAtualizarOitava) {
        btnAtualizarOitava.addEventListener("click", function () {

            if (!selectOitava.value) {
                alert("Selecione um jogo.");
                return;
            }

            const id_jogo = parseInt(selectOitava.value);

            const gols_mandante =
                parseInt(document.getElementById("golsMandanteOitava").value) || 0;

            const gols_visitante =
                parseInt(document.getElementById("golsVisitanteOitava").value) || 0;

            const penaltis_mandante =
                document.getElementById("penaltisMandante").value || null;

            const penaltis_visitante =
                document.getElementById("penaltisVisitante").value || null;

            fetch("/api/oitavas/placar", {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    id_jogo,
                    gols_mandante,
                    gols_visitante,
                    penaltis_mandante,
                    penaltis_visitante
                })
            })
            .then(res => res.json())
            .then(data => {
                alert(data.mensagem || data.erro);
                carregarOitavas();
            })
            .catch(error => console.error("Erro ao atualizar oitavas:", error));
        });
    }

    // ======================================
    // INICIALIZAÇÃO
    // ======================================

    carregarGrupo();
    carregarOitavas();


    async function carregarQuartas() {

        const response = await fetch("/api/quartas");
        const quartas = await response.json();

        const container = document.getElementById("quartas-container");
        container.innerHTML = "";

        quartas.forEach(jogo => {

            const div = document.createElement("div");

            div.innerHTML = `
                <hr>
                <p><strong>${jogo.mandante} x ${jogo.visitante}</strong></p>

                <input type="number" placeholder="Gols ${jogo.mandante}" id="gm_${jogo.id_jogo}">
                <input type="number" placeholder="Gols ${jogo.visitante}" id="gv_${jogo.id_jogo}">
                <br>
                <input type="number" placeholder="Pênaltis ${jogo.mandante}" id="pm_${jogo.id_jogo}">
                <input type="number" placeholder="Pênaltis ${jogo.visitante}" id="pv_${jogo.id_jogo}">
                <br>
                <button onclick="atualizarQuartas(${jogo.id_jogo})">
                    Atualizar Placar
                </button>
            `;

            container.appendChild(div);
        });
    }


    async function atualizarQuartas(id_jogo) {

        const dados = {
            id_jogo: id_jogo,
            gols_mandante: parseInt(document.getElementById(`gm_${id_jogo}`).value),
            gols_visitante: parseInt(document.getElementById(`gv_${id_jogo}`).value),
            penaltis_mandante: document.getElementById(`pm_${id_jogo}`).value || null,
            penaltis_visitante: document.getElementById(`pv_${id_jogo}`).value || null
        };

        const response = await fetch("/api/quartas/placar", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(dados)
        });

        const resultado = await response.json();
        alert(resultado.mensagem || resultado.erro);
    }



});
