# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTyperSlim(PythonPackage):
    """Typer, build great CLIs. Easy to code. Based on Python type hints."""
    
    homepage = "https://github.com/fastapi/typer"
    pypi = "typer-slim/typer_slim-0.16.0-py3-none-any.whl" 

    version("0.0.1", sha256="62e2522ed7d622777af7e05e0f32d7a1399d64b3f3b020c2274e346f9650cbfe", expand=False, url="https://files.pythonhosted.org/packages/ee/87/22944fb67b47511143c012bb7809e7f97eff33157a274ade2cb4ca2f2e92/typer_slim-0.0.1-py3-none-any.whl")
    version("0.12.0", sha256="ddd7042b29a32140528caa415750bcae54113ba0c32270ca11a6f64069ddadf9", expand=False, url="https://files.pythonhosted.org/packages/9e/8d/cd24db348ffdec4e2331c293f63eb8492956879c0925dd05d1e747b49cc7/typer_slim-0.12.0-py3-none-any.whl")
    version("0.12.1", sha256="a3feb4dd7928ab631089277604cf4a971f266b9fa9f1a2b9b0d68aa50b3b6fa5", expand=False, url="https://files.pythonhosted.org/packages/d2/f9/a19087c00b7e573259dfd60ad090d4a03963ab42b6cbec60e1a9eac2eab6/typer_slim-0.12.1-py3-none-any.whl")
    version("0.12.1.dev1", sha256="6ed919ed667f3c4b06c1f563947e4dbea9eb9285184d76d777067e1e1f1bab2a", expand=False, url="https://files.pythonhosted.org/packages/dc/e9/8bfb4ac7a4770086721f42b6e9efb704e7e3b6e7e4a7d8765a432035ecf4/typer_slim-0.12.1.dev1-py3-none-any.whl")
    version("0.12.1.dev2", sha256="e2efa57d7a41c0aa8a2b952aab1916da0f231a1d44cb32e197f0dc5ad73f594c", expand=False, url="https://files.pythonhosted.org/packages/58/15/81dde542f3034e45e4e2c1a93af5f234d254c85e985e6bdaec8668298dc4/typer_slim-0.12.1.dev2-py3-none-any.whl")
    version("0.12.2", sha256="6dc665472f7929ae32ac3dcaf5b3efce1caf39829d0506358d2d56d4962ab207", expand=False, url="https://files.pythonhosted.org/packages/85/03/c94585d50d77d5fa3f724682a847bd26f1e39a63431dab0a61cc5f01313c/typer_slim-0.12.2-py3-none-any.whl")
    version("0.12.3", sha256="142c73d91ac1df79a49cec5a1c2210c00b1b4040a91014b539792af5ba81c65c", expand=False, url="https://files.pythonhosted.org/packages/a3/ea/b4e1bdee4b6be51354b72699629398688e6ec794060adec9f588d97ef2d4/typer_slim-0.12.3-py3-none-any.whl")
    version("0.12.4", sha256="790a9cd6589494ce063a178473ccdad878fa36bc03f428710f5864670e988144", expand=False, url="https://files.pythonhosted.org/packages/b8/96/7a182808231c66dcd6f5c3239d9b73af29987588e748403ae97f1522a728/typer_slim-0.12.4-py3-none-any.whl")
    version("0.12.5", sha256="9a994f721b828783dbf144e17461b1c720bb4598e0d5eff7c1b3f08ee58cb062", expand=False, url="https://files.pythonhosted.org/packages/98/d4/ced1f8074819b43804a0a5015f33bae422330e8d38b1992be91fa947190c/typer_slim-0.12.5-py3-none-any.whl")
    version("0.12.dev1", sha256="0c18ac8f97c03a683e53070d1c7db5eb1195a7a39606700df7d8d9b9f05aef19", expand=False, url="https://files.pythonhosted.org/packages/16/04/25cd004c3a967b6cfbedf46ca6d46355b56e6352e1acb2a9744ec07e6ed1/typer_slim-0.12.dev1-py3-none-any.whl")
    version("0.12.dev2", sha256="d3fc23a598df5011f05ae2e6338231d6ab5a871fe49aa6bb2396f0872de13f0b", expand=False, url="https://files.pythonhosted.org/packages/aa/9b/6d99298386aa5fc092dcebca158f18df3d1cdd3c8036598ec2ca66880e54/typer_slim-0.12.dev2-py3-none-any.whl")
    version("0.13.0", sha256="33aad8029b717ee98228315f208cfae2f247765796f243ca314cb09fd652dc44", expand=False, url="https://files.pythonhosted.org/packages/a5/2c/f239c0b214617b1eefef76c81a8b98765716df665b5ac87b6cd1aeda800a/typer_slim-0.13.0-py3-none-any.whl")
    version("0.13.1", sha256="13f23cf414fb3de3d9163c4beebe0c6569eabcb85b71c89ffe42887a5332eb3b", expand=False, url="https://files.pythonhosted.org/packages/b6/f8/d44ccac8b4c09185f0c153d6fd31f02cd1d9a51cfeffde8384913de71e94/typer_slim-0.13.1-py3-none-any.whl")
    version("0.14.0", sha256="710d23c5956583aed4662871df759232f38f30bfa2c91b1aea54e4a1ce027c54", expand=False, url="https://files.pythonhosted.org/packages/80/a7/742592cdc96dbd3087cff1db8288450ae48aafb5774ba9138e73622727a2/typer_slim-0.14.0-py3-none-any.whl")
    version("0.15.0", sha256="2d1f220c708d4f81c99494d4416389298b5acb463700e74d345cb78edd095b03", expand=False, url="https://files.pythonhosted.org/packages/ed/99/f3b75f4b0da2edf8933f7a20a0c777edf65625676b6eac60e623c5267f7a/typer_slim-0.15.0-py3-none-any.whl")
    version("0.15.1", sha256="20233cb89938ea3cca633afee10b906a1b0e7c5330f31ed8c55f4f0779efe6df", expand=False, url="https://files.pythonhosted.org/packages/1f/7b/032ecd581e2170513bb6dc3cdb2581e20fdb94a272bae70fe93f2bca580b/typer_slim-0.15.1-py3-none-any.whl")
    version("0.15.2", sha256="4273014a3378b24367bffed45c2ce8dd3d85bd201a6f02e51ba6b19f336009be", expand=False, url="https://files.pythonhosted.org/packages/9e/84/9b68e98bf7417d25e38b27a0296bfcbc6719b15d7000f4c09d9716fa9d11/typer_slim-0.15.2-py3-none-any.whl")
    version("0.15.3", sha256="626c125b1b01eebafdc2bb12326b401863d1c4752342e3f9c1d9f829939fe300", expand=False, url="https://files.pythonhosted.org/packages/92/b1/0f3d4f3e35fd82248ed5bcb70c6249baebb39f0ab3faf7f9818101eec991/typer_slim-0.15.3-py3-none-any.whl")
    version("0.15.4", sha256="6d134e1b048da37ceacc1ccc3ad28a6f966c8f0833cc1513cf12a21de0da8ed8", expand=False, url="https://files.pythonhosted.org/packages/b6/7f/44304801838529b1051e00fb30e1750cacd10da31da1f3b0fa0e96ae6045/typer_slim-0.15.4-py3-none-any.whl")
    version("0.16.0", sha256="8aa94eef73b876506b9d239cd70cfedefac95541be8f060688aabfc800f53d67", expand=False, url="https://files.pythonhosted.org/packages/41/2d/dc1f0c872615aef018783408ac993be7832726a4b30032e317e9f2858267/typer_slim-0.16.0-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-click", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))

# {'click>=8.0.0': ['0.12.0', '0.12.1', '0.12.1.dev1', '0.12.1.dev2', '0.12.2', '0.12.3', '0.12.4', '0.12.5', '0.12.dev1', '0.12.dev2', '0.13.0', '0.13.1', '0.14.0', '0.15.0', '0.15.1', '0.15.2', '0.15.3', '0.16.0'], 'typing-extensions>=3.7.4.3': ['0.12.0', '0.12.1', '0.12.1.dev1', '0.12.1.dev2', '0.12.2', '0.12.3', '0.12.4', '0.12.5', '0.12.dev1', '0.12.dev2', '0.13.0', '0.13.1', '0.14.0', '0.15.0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.16.0'], 'shellingham>=1.3.0;extra=="all"': ['0.12.0', '0.12.dev1', '0.12.dev2'], 'rich>=10.11.0;extra=="all"': ['0.12.0', '0.12.dev1', '0.12.dev2'], 'shellingham>=1.3.0;extra=="standard"': ['0.12.0', '0.12.1', '0.12.1.dev1', '0.12.1.dev2', '0.12.2', '0.12.3', '0.12.4', '0.12.5', '0.12.dev1', '0.12.dev2', '0.13.0', '0.13.1', '0.14.0', '0.15.0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.16.0'], 'rich>=10.11.0;extra=="standard"': ['0.12.0', '0.12.1', '0.12.1.dev1', '0.12.1.dev2', '0.12.2', '0.12.3', '0.12.4', '0.12.5', '0.12.dev1', '0.12.dev2', '0.13.0', '0.13.1', '0.14.0', '0.15.0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.16.0'], 'click<8.2,>=8.0.0': ['0.15.4']}