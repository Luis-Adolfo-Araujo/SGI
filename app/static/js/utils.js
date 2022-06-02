function handleLogOut() {

  fetch(`${window.origin}/logout`, {
    method: "POST",
    credentials: "include", //insert cookies in the page
    body: '', 
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  }).then(function (response) {
      if (response.status !== 200){
        console.log(response.status)
        return
      } else {
        window.location.href = ""
      }
    })
  }

  async function loadIntoTable(url, table){
    let tHead = document.querySelector('thead')
    let tData = document.querySelector('tbody')
    let response = await fetch(url)
    let data = await response.json();
    data = JSON.stringify(data);
    
    // clear table
    tHead.innerHTML = "<tr></tr>";
    tData.innerHTML = "";
    
    let json = JSON.parse(data)
    
    // populate headers
    // define a table header from response
    // associate text with headerText and append it to tHead which is a table header html element
    for (const headerText of json[0].headers) {
      const headerElement = document.createElement("th");
      headerElement.textContent = headerText;
      tHead.querySelector("tr").appendChild(headerElement)
    } 
    
    for (const row of Object.values(json)) {
      console.log(row)
      values = Object.values(row)
      const rowElement = document.createElement("tr");
      
      
      for (const textItem of values) {
        if (typeof(textItem) === 'object'){
          continue
        }
        const dataElement = document.createElement("td");
        dataElement.textContent = textItem;
        rowElement.appendChild(dataElement);
      }

      tData.appendChild(rowElement)
    }
  }