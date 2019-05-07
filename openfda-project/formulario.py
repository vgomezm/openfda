<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>OpenFDA-project</title>
</head>
<body>

<form action = "listDrugs" method="get">
  <input type="submit" value="Listar fármacos">
    Limite: <input type="text" name="limit" value="1">
</form>

<form action = "listCompanies" method="get">
  <input type="submit" value="Listar empresas">
    Limite: <input type="text" name="limit" value="1">
</form>

<form action = "listWarnings" method="get">
  <input type="submit" value="Listar Advertencias">
    Limite: <input type="text" name="limit" value="1">
</form>

<form action = "searchDrug" method="get">
  <input type="submit" value="Buscar fármaco">
    Campo: <input type="text" name="active_ingredient" value="">
    Limite: <input type="text" name="limit" value="1">
</form>

<form action = "searchCompany" method="get">
  <input type="submit" value="Buscar empresas">
    Campo: <input type="text" name="company" value="">
    Limite: <input type="text" name="limit" value="1">
</form>

</body>
</html>
