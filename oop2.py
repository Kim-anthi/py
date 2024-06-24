class watu:
    def __init__(self, jina, miaka, urefu):
        self.jina = jina
        self.miaka = miaka
        self.urefu = urefu


    def __kuonyesha__(self):
        print(self.jina, self.miaka, self.urefu)


mywatu = watu('Abunuwasi', '20', '5 feet')
mywatu.__kuonyesha__()
