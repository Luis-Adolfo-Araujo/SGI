function handleLogOut() {
  fetch(`${window.origin}/logout`, {
    method: "POST",
    credentials: "include", //insert cookies in the page
    body: "",
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json",
    }),
  }).then(function (response) {
    if (response.status !== 200) {
      console.log(response.status);
      return;
    } else {
      window.location.href = "";
    }
  });
}

function makeUserGrid(column, dataUrl) {
  new gridjs.Grid({
    columns: column,
    server: {
      url: dataUrl,
      then: (data) =>
        data.map((card) => [
          card.ativo,
          card.email,
          card.login,
          card.nome,
          card.permissoes_id,
        ]),
      handle: (res) => {
        console.log(res);
        if (res.status === 404) return { data: [] };
        if (res.ok) return res.json();
        throw Error("something went wrong");
      }
      
    },
    pagination: {
      enabled: true,
      limit: 10,
      summary: false
    },
    search: {
      enabled: true
    },
    sort: true
  }).render(document.getElementById("wrapper"));
}

function makeMaterialGrid(column, dataUrl) {
  new gridjs.Grid({
    columns: column,
    server: {
      url: dataUrl,
      then: (data) =>
        data.map((card) => [
          card.estoque_minimo,
          card.fabricante_id,
          card.grupo_id,
          card.modelo,
          card.ncm,
          card.foto,
          card.possui_numero_serie,
          card.posicao_estoque,
          card.tipo_id
        ]),
      handle: (res) => {
        if (res.status === 404) return { data: [] };
        if (res.ok) return res.json();
        throw Error("something went wrong");
      },
    },
    pagination: {
      enabled: true,
      limit: 10,
      summary: false
    },
    search: {
      enabled: true
    },
    sort: true
  }).render(document.getElementById("wrapper"));
}

function makeProviderGrid(column, dataUrl) {
  new gridjs.Grid({
    columns: column,
    server: {
      url: dataUrl,
      then: (data) =>
        data.map((card) => [
          card.nome,
          card.nome_fantasia,
          card.cnpj,
          card.logradouro,
          card.bairro,
          card.cidade,
          card.numero,
          card.cep,
          card.uf,
          card.nome_contato1,
          card.nome_contato2,
          card.fone_contato1,
          card.fone_contato2,
          card.email_contato1,
          card.email_contato2,
          card.situacao
        ]),
      handle: (res) => {
        if (res.status === 404) return { data: [] };
        if (res.ok) return res.json();
        throw Error("something went wrong");
      },
    },resizable: true,
    pagination: {
      enabled: true,
      limit: 10,
      summary: false
    },
    search: {
      enabled: true
    },
    sort: true
  }).render(document.getElementById("wrapper"));
}

function createEditLink(rowElement) {
  let dataElement = document.createElement("a");
  let icon = document.createElement("i");
  icon.className = "fas fa-edit";
  icon.style = "padding-top: 15px; padding-left: 8px; color: grey";
  // dataElement.href = 'userGrid/editUser/';
  dataElement.appendChild(icon);
  return rowElement.appendChild(dataElement);
}

function createRemoveLink(rowElement) {
  dataElement = document.createElement("a");
  icon = document.createElement("i");
  icon.className = "fas fa-trash";
  icon.style = "padding-left: 3px; color: #d9534f";
  dataElement.appendChild(icon);
  return rowElement.appendChild(dataElement);
}
