document.addEventListener("DOMContentLoaded", function () {

    const tabs = document.querySelectorAll(".tab-btn");
    const contents = document.querySelectorAll(".tab-content");

    // Alternar abas
    tabs.forEach(tab => {
        tab.addEventListener("click", () => {

            tabs.forEach(t => t.classList.remove("active"));
            contents.forEach(c => c.classList.remove("active"));

            tab.classList.add("active");
            document.getElementById(tab.dataset.tab).classList.add("active");
        });
    });

    // =========================
    // Carregar todos os grupos
    // =========================
    document.getElementById("btnTodos").addEventListener("click", function () {

        fetch("/api/classificacao")
            .then(res => res.json())
            .then(data => {

                let html = "";

                for (let grupo in data) {

                    html += `<h2>Grupo ${grupo}</h2>`;
                    html += montarTabela(data[grupo]);
                }

                document.getElementById("tabelaTodos").innerHTML = html;
            });
    });

    // =========================
    // Carregar grupo específico
    // =========================
    document.getElementById("btnGrupo").addEventListener("click", function () {

        fetch("/api/classificacao")
            .then(res => res.json())
            .then(data => {

                const grupo = document.getElementById("grupoPublico").value;

                document.getElementById("tabelaGrupo").innerHTML =
                    montarTabela(data[grupo]);
            });
    });

    function montarTabela(grupo) {

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

        return tabela;
    }

});
