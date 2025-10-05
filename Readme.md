# TCC - IFSC - Eng. Telecom TCC

Este repositório é dedicado ao desenvolvimento do meu Trabalho de Conclusão de Curso (TCC) para o curso de Engenharia de Telecomunicações no Instituto Federal de Santa Catarina (IFSC).

### Autor: Arthur Cadore Matuella Barcella

## Instalação: 

Para compilar o projeto, você precisará do `make` e do `texlive-full`. Instale-os com o comando:

```bash
sudo apt-get update && sudo apt-get install -y make texlive-full
git clone
cd monografia-tcc
make 
```

Em seguida, instale o pacote `biblatex-abnt`, que não está disponível nos repositórios do Ubuntu. Para isso, execute os comandos abaixo:

```bash
mkdir -p ~/texmf/tex/latex/biblatex-abnt
cd ~/texmf/tex/latex/biblatex-abnt

wget https://mirrors.ctan.org/macros/latex/contrib/biblatex-contrib/biblatex-abnt.zip
unzip biblatex-abnt.zip
rm biblatex-abnt.zip

texhash ~/texmf
```

Por fim, edite os arquivos `.tex` conforme necessário e compile novamente, para isso, recomedo utilizar a extensão LaTeX Workshop do VSCode.

```json 
		"vscode": {
			"extensions": [
				"James-Yu.latex-workshop"
			]
		}
```

## Referências:

- [Modelo de TCC - Prof Emerson Mello](https://github.com/emersonmello/monografia-latex-ifsc)