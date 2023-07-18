
```markdown
# Projeto de Dashboard do Google Analytics para Acompanhamento de Vendas

Este projeto consiste em um Dashboard desenvolvido no Power BI para realizar o acompanhamento de vendas de um site usando dados do Google Analytics. O Dashboard foi projetado no Figma no modo DARK para uma experiência visual agradável.

## Funcionalidades

- Visualização de métricas-chave de vendas, como receita, número de transações
- Comparação de desempenho com períodos anteriores usando dados históricos.

## Configuração

1. Clone este repositório em sua máquina local.
2. Importe o arquivo `.pbix` no Power BI Desktop para abrir o Dashboard.
3. Conecte o Power BI Desktop à sua conta do Google Analytics para obter os dados.
4. Faça as personalizações necessárias no Dashboard de acordo com suas preferências.

## Requisitos

- Power BI Desktop: [Download](https://powerbi.microsoft.com/desktop/)
- Conta do Google Analytics com acesso aos dados do site em questão

## Visualização do Dashboard

![Dashboard Preview](dashboard_preview.png)

## Atualização Automática

Para manter as informações sempre atualizadas, foi implementado um loop em Python que atualiza o Dashboard no navegador a cada 3 minutos. Isso garante que os dados exibidos estejam sempre sincronizados com as informações mais recentes do Google Analytics.

Para executar o loop de atualização automática, siga estas etapas:

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as dependências necessárias executando `pip install -r requirements.txt`.
3. Execute o script `update_dashboard.py` usando o comando `python update_dashboard.py`.

## Contribuição

Contribuições são bem-vindas! Se você tiver alguma sugestão, correção de bugs ou melhorias para este projeto, fique à vontade para abrir uma "issue" ou enviar uma "pull request".

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
```

Lembre-se de incluir uma imagem do preview do Dashboard (`dashboard_preview.png`) no diretório do projeto e uma seção de licença, conforme aplicável.

Certifique-se de personalizar as seções de configuração e requisitos com as informações relevantes para o seu projeto.
