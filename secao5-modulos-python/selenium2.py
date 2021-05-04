from selenium import webdriver
from time import sleep

# O intuito deste teste foi o de treinar a automatização de procedimentos no navegador Firefox.
# Descrição dos passos:
# 1º: Acessar o site da Amazon
# 1º: Preencher o campo de busca com um produto qualquer (neste caso, um livro)
# 1º: Selecionar o segundo produto da lista de resultados
# 1º: Inserir esse produto no carrinho de compras
# 1º: Visualizar o carrinho com o produto inserido
# 1º: Fechar o navegador

class MozillaAuto:
    def __init__(self):
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.browser = webdriver.Firefox(
            executable_path='caminho-do-arquivo/geckodriver',
            options=self.options)

    def acessa_site(self, url):
        self.browser.get(url)

    def tela_cheia(self):
        self.browser.maximize_window()

    def pesquisa_produtos(self, pesquisa):
        barra = self.browser.find_element_by_css_selector(
            '#twotabsearchtextbox')
        confirma = self.browser.find_element_by_id('nav-search-submit-button')

        barra.send_keys(pesquisa)
        confirma.click()

    def seleciona_livro(self):
        livro = self.browser.find_element_by_css_selector('div.sg-col-4-of-12:nth-child(5) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > h2:nth-child(1) > a:nth-child(1)')
        livro.click()

    def coloca_no_carrinho(self):
        btn = self.browser.find_element_by_id('submit.add-to-cart')
        btn.click()

    def olha_carrinho(self):
        carrinho = self.browser.find_element_by_id('nav-cart-count')
        carrinho.click()
        sleep(7)

    def fecha_browser(self):
        self.browser.quit()


if __name__ == "__main__":

    firefox = MozillaAuto()

    firefox.acessa_site('https://www.amazon.com.br/')
    firefox.tela_cheia()

    firefox.pesquisa_produtos('livros python')
    firefox.seleciona_livro()
    firefox.coloca_no_carrinho()
    firefox.olha_carrinho()

    firefox.fecha_browser()
