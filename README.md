# devops-bootcamp-tareaC8
- Instalar AWS CLI
- Instalar jq y curl en el sistema operativo
- Con el siguiente comando como base: 

<pre lang="markdown">aws ec2.describe-security-groups |jq .SecurityGroups[].GroupId </pre>
1. Hacer la averiguación de lo que hace el comando.
2. Escribir un archivo python que realice la misma función.




**1. Descripción del comando**

El comando permite obtener una lista de todos los security groups de la cuenta AWS en la región configurada, devolviendo un JSON grande con mucha información por grupo. Luego con jq se extrae solo los valores del campo GroupId de cada security group.

    aws ec2 describe-security-groups
- Usa la AWS CLI para obtener una lista de todos los security groups de tu cuenta, en la región configurada.
- Devuelve un JSON grande con mucha información por grupo (ID, reglas, nombre, etc.).


<pre lang="markdown"> | jq .SecurityGroups[].GroupId </pre>

- Usa jq (herramienta de línea de comandos para procesar JSON) para extraer solo los valores del campo GroupId de cada security group.
- SecurityGroups[] accede al array, y .GroupId obtiene el ID de cada uno.
