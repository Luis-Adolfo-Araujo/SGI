  $(function () {
    $("#materialGrid").jsGrid({
      height: "100%",
      width: "100%",

      sorting: true,
      paging: true,

      data: db.clients,

      fields: [
        { name: "Fabricante", type: "text", width: 150 },
        { name: "Tipo", type: "number", width: 150 },
        { name: "Grupo", type: "text", width: 200 },
        { name: "Modelo", type: "select", items: db.countries, valueField: "Id", textField: "Name", width: 100 },
        { name: "NCM", type: "text", width: 150 },
        { name: "Estoque Min.", type: "number",},
        { name: "Posiçao no Estoque", type: "number"},
        { name: "Foto", type: "text", title: "Ativo"},
        { name: "Possui N˚ série?", type: "checkbox"}
      ]
    });
  });
  $(function () {
    $("#movimentacaoGrid").jsGrid({
      height: "100%",
      width: "100%",

      sorting: true,
      paging: true,

      data: db.clients,

      fields: [
        { name: "Fornecedor", type: "text", width: 150 },
        { name: "Usuário", type: "number", width: 150 },
        { name: "Tipo", type: "text", width: 200 },
        { name: "Data|Hora", type: "select", items: db.countries, valueField: "Id", textField: "Name", width: 100 },
        { name: "Quantidade", type: "text", width: 150 },
        { name: "Valor", type: "number",},
        { name: "Descrição", type: "number"}
      ]
    });
  });
  $(function () {
    $("#providerGrid").jsGrid({
      height: "100%",
      width: "100%",

      sorting: true,
      paging: true,

      data: db.clients,

      fields: [
        { name: "Nome", type: "text", width: 150 },
        { name: "Nome Fantasia", type: "number", width: 150 },
        { name: "CNPJ", type: "text", width: 200 },
        { name: "Logradouro", type: "select", items: db.countries, valueField: "Id", textField: "Name", width: 100 },
        { name: "bairro", type: "text", width: 150 },
        { name: "cidade", type: "number",},
        { name: "numero", type: "number"},
        { name: "CEP", type: "number",},
        { name: "UF", type: "number",},
        { name: "Nome Contato 1", type: "number",},
        { name: "Nome Contato 2", type: "number",},
        { name: "fone Contato 1", type: "number",},
        { name: "fone Contato 2", type: "number",},
        { name: "email Contato 1", type: "number",},
        { name: "email Contato 2", type: "number",},
        { name: "Situação", type: "text",},
        
      ]
    });
  });
  $(function () {
    $("#manufacturerGrid").jsGrid({
      height: "100%",
      width: "100%",

      sorting: true,
      paging: true,

      data: db.clients,

      fields: [
        { name: "Nome", type: "text", width: 150 },
        { name: "Nome Fantasia", type: "number", width: 150 },
        { name: "CNPJ", type: "text", width: 200 },
        { name: "Logradouro", type: "select", items: db.countries, valueField: "Id", textField: "Name", width: 100 },
        { name: "bairro", type: "text", width: 150 },
        { name: "cidade", type: "number",},
        { name: "numero", type: "number"},
        { name: "CEP", type: "number",},
        { name: "UF", type: "number",},
        { name: "Nome Contato 1", type: "number",},
        { name: "Nome Contato 2", type: "number",},
        { name: "fone Contato 1", type: "number",},
        { name: "fone Contato 2", type: "number",},
        { name: "email Contato 1", type: "number",},
        { name: "email Contato 2", type: "number",},
        { name: "Situação", type: "text",},
        
      ]
    });
  });
