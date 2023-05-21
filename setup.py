from setuptools import setup, find_packages

setup(
    name='pitonbr',
    version='1.0.0',
    description='A biblioteca Píton é uma ferramenta educacional para falantes de português que desejam aprender programação em Python. Com sintaxe próxima ao Portugol, ela oferece uma abordagem amigável e acessível, tornando o aprendizado de algoritmos e lógica de programação mais acessível para quem tem dificuldades com o inglês.',
    author='Dux Tecnologia',
    author_email='contato@dux.tec.br',
    url='https://github.com/duxtec/piton',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
