import http.server
import socketserver
import json

PUERTO = 8000
FORMULARIO = 'formulario.py'
socketserver.TCPServer.allow_reuse_address = True
NOMBRE_SERVIDOR = "api.fda.gov"
NOMBRE_RECURSO = "/drug/label.json"
headers = {'User-Agent': 'http-client'}


class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def mostrar_formulario(self, formulario):
        """Esta función devuelve el formulario principal"""

        with open(formulario, "r") as f:
            return f.read()

    def searchDrug(self, active_ingredient, limit):
        """Esta función devuelve todos los fármacos cuyo ingrediente
        activo es active_ingredient"""
        consulta=""
        message = (' <!DOCTYPE html>\n'
            '<html lang="es">\n'
            '<head>\n'
            '    <meta charset="UTF-8">\n'
            '</head>\n'
            '<body>\n'
            '<ul>\n')
        # Establecer conexión con el servidor
        conexion = http.client.HTTPSConnection(NOMBRE_SERVIDOR)
        # Construir la consulta al servidor
        if active_ingredient:
          consulta = NOMBRE_RECURSO + "?search=active_ingredient:" + str(active_ingredient) + "&limit=" + str(limit)
        # Enviar la consulta al servidor
        conexion.request("GET", consulta, None, headers)
        # Obtener la respuesta del servidor
        respuesta = conexion.getresponse()


        if respuesta.status == 404:
          message+= ("<h1>ERROR 404. Fármaco no encontrado</h1>" +
                    '</ul>\n'
                    '\n'
                    '<a href="/">Home</a>'
                    '</body>\n'
                    '</html>')
          return message, 404


        # Transformar la respuesta a json
        drugs = json.loads(respuesta.read().decode("utf-8"))
        conexion.close()

        for drug in drugs['results']:
            if drug['openfda']:
                nombre = drug['openfda']['substance_name'][0]
                marca = drug['openfda']['brand_name'][0]
                fabricante = drug['openfda']['manufacturer_name'][0]
            else:
                nombre = "Desconocido"
                marca = "Desconocido"
                fabricante = "Desconocido"

            message += ("<li> Nombre: " + nombre +
                           " / Marca: " + marca +
                           " / Fabricante: " + fabricante +
                        "</li>\n")

        # Cierre del html
        message += ('</ul>\n'
                    '\n'
                    '<a href="/">Home</a>'
                    '</body>\n'
                    '</html>')

        return message, 200


    def searchCompany(self, company_name, limit):
        """Esta función devuelve todas las empresas cuyo nombre
        es company_name"""
        consulta=""
        message = (' <!DOCTYPE html>\n'
            '<html lang="es">\n'
            '<head>\n'
            '    <meta charset="UTF-8">\n'
            '</head>\n'
            '<body>\n'
            '<ul>\n')
        # Establecer conexión con el servidor
        conexion = http.client.HTTPSConnection(NOMBRE_SERVIDOR)
        # Construir la consulta al servidor
        if company_name:
          consulta = NOMBRE_RECURSO + "?search=openfda.manufacturer_name:" + str(company_name) + "&limit=" + str(limit)

        # Enviar la consulta al servidor
        conexion.request("GET", consulta, None, headers)
        # Obtener la respuesta del servidor
        respuesta = conexion.getresponse()


        if respuesta.status == 404:
          message+= ("<h1>ERROR 404. Empresa no encontrada</h1>" +
                    '</ul>\n'
                    '\n'
                    '<a href="/">Home</a>'
                    '</body>\n'
                    '</html>')
          return message, 404


        # Transformar la respuesta a json
        drugs = json.loads(respuesta.read().decode("utf-8"))
        conexion.close()

        for drug in drugs['results']:
            if drug['openfda']:
                fabricante = drug['openfda']['manufacturer_name'][0]
            else:
                fabricante = "Desconocido"
            message += ("<li> " + fabricante +
                        "</li>\n")

        # Cierre del html
        message += ('</ul>\n'
                    '\n'
                    '<a href="/">Home</a>'
                    '</body>\n'
                    '</html>')

        return message, 200

    def listDrugs(self, limit):
        """Esta función devuelve una lista de fármacos"""
        consulta=""
        message = (' <!DOCTYPE html>\n'
            '<html lang="es">\n'
            '<head>\n'
            '    <meta charset="UTF-8">\n'
            '</head>\n'
            '<body>\n'
            '<ul>\n')
        # Establecer conexión con el servidor
        conexion = http.client.HTTPSConnection(NOMBRE_SERVIDOR)
        # Construir la consulta al servidor
        consulta = NOMBRE_RECURSO + "?limit=" + str(limit)

        # Enviar la consulta al servidor
        conexion.request("GET", consulta, None, headers)
        # Obtener la respuesta del servidor
        respuesta = conexion.getresponse()

        # Transformar la respuesta a json
        drugs = json.loads(respuesta.read().decode("utf-8"))
        conexion.close()


        for drug in drugs['results']:
            if drug['openfda']:
                nombre = drug['openfda']['substance_name'][0]
                marca = drug['openfda']['brand_name'][0]
                fabricante = drug['openfda']['manufacturer_name'][0]
            else:
                nombre = "Desconocido"
                marca = "Desconocido"
                fabricante = "Desconocido"

            message += ("<li> Nombre: " + nombre +
                           " / Marca: " + marca +
                           " / Fabricante: " + fabricante +
                        "</li>\n")

        # Cierre del html
        message += ('</ul>\n'
                    '\n'
                    '<a href="/">Home</a>'
                    '</body>\n'
                    '</html>')

        return message


    def listCompanies(self, limit):
        """Esta función devuelve una lista de empresas"""
        consulta=""
        message = (' <!DOCTYPE html>\n'
            '<html lang="es">\n'
            '<head>\n'
            '    <meta charset="UTF-8">\n'
            '</head>\n'
            '<body>\n'
            '<ul>\n')
        # Establecer conexión con el servidor
        conexion = http.client.HTTPSConnection(NOMBRE_SERVIDOR)
        # Construir la consulta al servidor
        consulta = NOMBRE_RECURSO + "?limit=" + str(limit)

        # Enviar la consulta al servidor
        conexion.request("GET", consulta, None, headers)
        # Obtener la respuesta del servidor
        respuesta = conexion.getresponse()

        # Transformar la respuesta a json
        drugs = json.loads(respuesta.read().decode("utf-8"))
        conexion.close()


        for drug in drugs['results']:
            if drug['openfda']:
                fabricante = drug['openfda']['manufacturer_name'][0]
            else:
                fabricante = "Desconocido"

            message += ("<li> " + fabricante +
                        "</li>\n")

        # Cierre del html
        message += ('</ul>\n'
                    '\n'
                    '<a href="/">Home</a>'
                    '</body>\n'
                    '</html>')

        return message

    def listWarnings(self, limit):
        """Esta función devuelve una lista de advertencias"""
        consulta=""
        message = (' <!DOCTYPE html>\n'
            '<html lang="es">\n'
            '<head>\n'
            '    <meta charset="UTF-8">\n'
            '</head>\n'
            '<body>\n'
            '<ul>\n')
        # Establecer conexión con el servidor
        conexion = http.client.HTTPSConnection(NOMBRE_SERVIDOR)
        # Construir la consulta al servidor
        consulta = NOMBRE_RECURSO + "?limit=" + str(limit)

        # Enviar la consulta al servidor
        conexion.request("GET", consulta, None, headers)
        # Obtener la respuesta del servidor
        respuesta = conexion.getresponse()

        # Transformar la respuesta a json
        drugs = json.loads(respuesta.read().decode("utf-8"))
        conexion.close()


        for drug in drugs['results']:
            if 'warnings' in drug:
                warnings = drug['warnings'][0]
            elif 'warnings_and_cautions' in drug:
                warnings = drug['warnings_and_cautions'][0]
            else:
                warnings = "Desconocido"

            message += ("<li> " + warnings +
                        "</li>\n")

        # Cierre del html
        message += ('</ul>\n'
                    '\n'
                    '<a href="/">Home</a>'
                    '</body>\n'
                    '</html>')

        return message


    # GET. Este metodo se invoca automaticamente cada vez que hay una
    # peticion GET por HTTP. El recurso que nos solicitan se encuentra
    # en self.path
    def do_GET(self):
        limit = 10 # limite por defecto
        nombre = ""
        message = ""
        parametros = self.path.split('?')
        funcion = parametros[0] #obtener la función a la que hay que llamar

        #Obtener los argumentos
        if len(parametros) > 1:
          argumentos = parametros[1].split('&')
        else:
          argumentos = ""

        #Comprobar si el argumento es limite o un nombre
        if len(argumentos) > 0:
          if argumentos[0].split('=')[0] == "limit":
            limit = argumentos[0].split('=')[1]
          else:
            nombre = argumentos[0].split('=')[1]
            if len(argumentos) > 1:
                if argumentos[1].split('=')[0] == "limit":
                    limit = argumentos[1].split('=')[1]
        else:
          print("No hay argumentos")

        #Llamada a las funciones dependiendo de los parametros recibidos
        if funcion == '/redirect':
          self.send_response(302)
          self.send_header('Location', 'http://localhost:'+ str(PUERTO))
          self.end_headers()
  
        elif funcion == '/secret':
          self.send_response(401)
          self.send_header('WWW-Authenticate', "Basic realm = DENIED")
          self.end_headers()

        elif funcion == "/":
          message = self.mostrar_formulario(FORMULARIO)
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
          self.end_headers()
          self.wfile.write(bytes(message, "utf8"))
      
        elif funcion == "/searchDrug":
          message,status = self.searchDrug(nombre, limit)
          self.send_response(status)
          self.send_header('Content-type', 'text/html')
          self.end_headers()
          self.wfile.write(bytes(message, "utf8"))

        elif funcion == "/searchCompany":
          message,status = self.searchCompany(nombre, limit)
          self.send_response(status)
          self.send_header('Content-type', 'text/html')
          self.end_headers()
          self.wfile.write(bytes(message, "utf8"))

        elif funcion == "/listDrugs":
          message = self.listDrugs(limit)
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
          self.end_headers()
          self.wfile.write(bytes(message, "utf8"))

        elif funcion == "/listCompanies":
          message = self.listCompanies(limit)
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
          self.end_headers()
          self.wfile.write(bytes(message, "utf8"))

        elif funcion == "/listWarnings":
          message = self.listWarnings(limit)
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
          self.end_headers()
          self.wfile.write(bytes(message, "utf8"))

        else:
          self.send_response(404)
          self.end_headers()
          message = "<h1>ERROR 404. Los datos introducidos son incorrectos</h1>"
          self.wfile.write(bytes(message, "utf8"))


# Establecemos como manejador nuestra propia clase
Handler = testHTTPRequestHandler

# -- Configurar el socket del servidor, para esperar conexiones de clientes
with socketserver.TCPServer(("", PUERTO), Handler) as httpd:
    print("Escuchando en el puerto", PUERTO)

    # Entrar en el bucle principal
    # Las peticiones se atienden desde nuestro manejador
    # Cada vez que se ocurra un "GET" se invoca al metodo do_GET de
    # nuestro manejador
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Interrupción")

print("")
print("El servidor se ha parado")
