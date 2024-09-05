function deleteQuery(queryId) {
    fetch("/delete-query", {
      method: "POST",
      body: JSON.stringify({ queryId: queryId }),
    }).then((_res) => {
      window.location.href = "/home";
    });
  }