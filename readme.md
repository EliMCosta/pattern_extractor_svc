## Microsserviço Python para Extração de Padrões

### Estrutura do Projeto
```
pattern_extractor_svc/
│
├── src/
│   └── main.py
│
├── tests/
│   └── test_app.py
│
├── requirements.txt
└── Dockerfile
```

### Pré-requisitos
1. **Preparação**:
   - Certifique-se de que o Minikube esteja instalado e configurado corretamente em sua máquina local. Você pode iniciar o Minikube com o comando `minikube start`.
   - Certifique-se de que sua imagem do Docker esteja construída corretamente e esteja disponível. Se você estiver usando apenas o Minikube e não tiver um registro Docker privado, pode ser útil usar o ambiente Docker do Minikube para construir suas imagens, garantindo que elas estejam disponíveis para o Minikube. Você pode configurar isso com `eval $(minikube -p minikube docker-env)` antes de construir sua imagem Docker.

### Construindo a Imagem Docker

A partir da raiz do projeto, executar o comando:

```bash
eval $(minikube -p minikube docker-env) #Trabalhando com imagem local
docker build -t pattern_extractor_svc .
```

### Executando o Contêiner

Para fazer o deploy no Minikube:

#### Executando o Deployment e o Service

1. **Deploy do Microsserviço**:
   Execute o seguinte comando para criar o Deployment no Kubernetes:

   ```bash
   kubectl apply -f deployment.yaml
   ```

2. **Criação do Service**:
   Execute o seguinte comando para criar o Service e expor seu microsserviço:

   ```bash
   kubectl apply -f service.yaml
   ```

3. **Verificando o Estado**:
   Você pode verificar o estado do Deployment e do Service usando:

   ```bash
   kubectl get deployments
   kubectl get services
   kubectl get pods -l app=pattern-extractor
   kubectl logs <nome-do-pod>
   ```

4. **Acesso ao Microsserviço**:
   - Com o Service do tipo `NodePort`, você pode acessar seu microsserviço fora do cluster Minikube. Para encontrar a URL que você pode usar para acessar o serviço, execute:

     ```bash
     minikube service pattern-extractor-svc --url
     ```

     Isso fornecerá a URL que você pode usar para acessar seu microsserviço.

Isso mapeia a porta 8000 do host para a porta 80 do contêiner, permitindo que você acesse o microsserviço através de `http://{IP_HOST}:8000`.

### Testando o Serviço
   Após iniciar o servidor, você pode testar o serviço usando ferramentas como `curl`, Postman ou diretamente através do navegador acessando a documentação interativa gerada pelo FastAPI (`http://{IP_HOST}:8000/docs`).

   Exemplo de requisição `curl` a partir da máquina local:

   ```bash
   curl -X 'POST' \
     'http://127.0.0.1:8000/extrair-padroes/' \
     -H 'accept: application/json' \
     -H 'Content-Type: application/json' \
     -d '{
     "texto": "Meu CPF é 123.456.789-09, PIS 123.45678.12.3, Título 123456789012, CNH 52798802300, e-mail exemplo@dominio.com, CEP 12345-678, nasci em 01/01/1980, tel: (11) 98765-4321, placa ABC1D23.",
     "labels": ["E-mail", "PIS/PASEP", "Outros", "CPF", "CNH"]
   }'
   ```

 Dependendo do modelo do Spacy escolhido, os tipos de entidades disponíveis podem variar, então ajuste os parâmetros e o código conforme necessário.

### Excluindo o deployment
  ```bash
  kubectl delete deployment pattern-extractor-svc
  ```

Kubernetes v1.28.3 on Docker 24.0.7
