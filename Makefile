all: install 

install: 
	# install latex packages
	@echo "Installing LaTeX packages..."
	sudo apt-get install texlive-full 
	@echo "Install the following LaTeX extension on Vscode:"
	@echo "Ctrl + P -> ext install James-Yu.latex-workshop"

