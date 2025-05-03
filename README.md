# devops-bootcamp-tareaC8
Instalar AWS CLI
Instalar jq y curl en el sistema operativo
Con el siguiente comando como base: 
aws ec2.describe-security-groups |jq .SecurityGroups[].GroupId
1. Hacer la averiguación de lo que hace el comando.
2. Escribir un archivo python que realice la misma función.

# Descripción del comando
aws ec2.describe-security-groups |jq .SecurityGroups[].GroupId
El comando permite obtener una lista de todos los security groups de la cuenta AWS en la región configurada, devolviendo un JSON grande con mucha información por grupo. Luego con jq se extrae solo los valores del campo GroupId de cada security group.
