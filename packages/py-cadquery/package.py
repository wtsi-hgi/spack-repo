# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os


class PyCadquery(PythonPackage):
    """CadQuery is a parametric  scripting language for creating and traversing CAD models"""
    
    homepage = "https://github.com/CadQuery/cadquery"
    pypi = "cadquery/cadquery-2.5.2-py3-none-any.whl" 

    version("0.1.0", sha256="9a7b264c1c603a15583903d6206c6b933c752c1d6fbd71eda1af7297da179d5e")
    version("0.1.1", sha256="8e7b1a49d2a5f1f42c47e154710a252a50b7ce6c43043f18d741c03204748a1a")
    version("0.1.2", sha256="5787183fac315a5583f60244f2c229be984771c50b75ee8026a630ae24f36c2e")
    version("0.1.3", sha256="9cae0911974949c69be2e14255b5e2ed75282b60ffaba189b6f8bd02666b671e")
    version("0.1.4", sha256="578d79d7c9804e9e222873c630c415497bc90558becd47b3472d8da1d976b217")
    version("0.1.5", sha256="06721c133fcecff197e3b19bfbd679c67379cdb9386009d8615798449a57831a")
    version("0.1.7", sha256="1f77870e059f003f5d5f5aac92f66119445b38549bff4644ee110c85d795ed3a")
    version("0.1.8", sha256="b5adb08bf1b9bd02a4ef2368054deedb7e0360940156b9253575c375f1a769f8")
    version("0.2.0", sha256="cb45da43808bb504c3b2bc6975523b3f372b34c77445661c8f7a89bc76da0c16")
    version("0.3.0", sha256="dafdc447153b433d1d4e55744618c8e5300d7dedb7318a16786a2d2af52ffcaf")
    version("0.4.0", sha256="1515e4444b5f64f523d35e9403a03db8f41b97d196c5bdcd33264ed45395aba6")
    version("0.4.185", sha256="fd5ec86866a35bce4dc6e0688f9428916b42f19ebf682a6f926c18aa6fe41ae8")
    version("0.4.186", sha256="c7b3ad1213e56b764ede47683faea31446de06e0f10b997fd201e570535ee30e")
    version("0.5.1", sha256="d36a8ef3b3b0c1761db4368628a1c6717bd651e9925993f2c0de6b4d3ed352fa")
    version("0.5.2", sha256="036a23775058a12290a53b5b6f71ece486933de615d5d1e1ddae529821d72d57")
    version("1.0.0", sha256="f91f8d7d938c1b7fd27f8e1e9a0c2a6d957f416fc12cad69bb167c77a1a525c6")
    version("1.1.0", sha256="cf505451362f40fb2271ddce1872dd1e5e668e00d9c183d346c9d8e88719c67c")
    version("1.2.0", sha256="9988adad97357a699128967bd379d9b8d63c8947e06c3584e6371df699363abc")
    version("1.2.1", sha256="e60d10ca0426a9c56854a7ddfdb0d03b0c5a6015d9a85a1b2f35e064dee1ba7a", expand=False, url="https://files.pythonhosted.org/packages/50/18/d068129d7f67e22b535a1fa4585b91bf6aaa4d9d1d3c5f4cb6fc24b4ec28/cadquery-1.2.1-py3-none-any.whl")
    version("1.2.2", sha256="f3d5d066922924e7fa3977efa5cd6068192cff49c12db2bb8b31ccd07be571d9", expand=False, url="https://files.pythonhosted.org/packages/38/4c/cd658673ef8f27fb2ba9f75d1ce8f7e3e3790c59bcbc879dc66698214832/cadquery-1.2.2-py3-none-any.whl")
    version("1.2.4", sha256="059517fd952f5e12e80001c0fa9494c51e1932a8a408014b78ccc11937c21463", expand=False, url="https://files.pythonhosted.org/packages/d0/52/02c17bc2dd4e4a6ebd2fb54b9899e21a90f9c10244d8c4639657153863f3/cadquery-1.2.4-py3-none-any.whl")
    version("1.2.5", sha256="879238ac572604cd35d4369bc7217504cc0ab2ceb044f67ba15575d0d7aae580", expand=False, url="https://files.pythonhosted.org/packages/93/4b/6e65ed63f0016cbe11c844a1b3bd86658db9a8138b1a3f7a572c38499eb7/cadquery-1.2.5-py3-none-any.whl")
    version("2.2.0", sha256="92855894e618192c1106f87a75569f464478074a635921c9b5cd415b66a3e17b", expand=False, url="https://files.pythonhosted.org/packages/ec/c8/b53bb330cc3d8378537ab9466aa520f2a7c46aa21f7f1832e33429d21b7b/cadquery-2.2.0-py3-none-any.whl")
    version("2.2.0b0", sha256="9e80404bff710f39419c998018d0406d30f9092cd020c86d4987b1c1c322718a", expand=False, url="https://files.pythonhosted.org/packages/9e/32/c647accb280fa97c9582b293fac1b3efb2c509729ff5c7d45d2c9e763c89/cadquery-2.2.0b0-py3-none-any.whl")
    version("2.2.0b1", sha256="4d847cfc02140a7baccfa7cdae5d302b7161e33b1d1750f63d7caa1787a45349", expand=False, url="https://files.pythonhosted.org/packages/fb/e4/c7271984344ec0fc30c6bc2adb0ddb4c3a4ab718448df4036a2573aeca7d/cadquery-2.2.0b1-py3-none-any.whl")
    version("2.2.0b2", sha256="3518e3f4da07635413b82d5beb63a0b6a70a70e67b983067e82e62cd434109c4", expand=False, url="https://files.pythonhosted.org/packages/55/7e/f444700f380f55aa40a82bea0eb65373ea4892214ae441d7de06d18f467a/cadquery-2.2.0b2-py3-none-any.whl")
    version("2.3.0", sha256="f03076ed775934bca97dcca7c110980513fab591d2420137300a5db1f261740f", expand=False, url="https://files.pythonhosted.org/packages/e2/bd/0b9914104b9a6e9fd75566c993ed6e97767735acffbab6997a29c3fd94c3/cadquery-2.3.0-py3-none-any.whl")
    version("2.3.1", sha256="2bdd3cc37639c5a9485d394d081334769c2b9e2fee6a42c0ca53e64fd9ff6a8d", expand=False, url="https://files.pythonhosted.org/packages/bd/a8/9878a90f9f0d31b14e1c86d70b3b5f499d921fc79a5e16b25b642dc32ccd/cadquery-2.3.1-py3-none-any.whl")
    version("2.4.0", sha256="66c865b1e5db205b81a5ddc8533d4741577291292cf2dc80b104ae9e3085b195", expand=False, url="https://files.pythonhosted.org/packages/af/19/3c2286e1bedc8ba2e9f916db1100e0275f2c202a279a6c7de8f11abe3156/cadquery-2.4.0-py3-none-any.whl")
    version("2.5.2", sha256="d9d375c702b1e599069a4f049f5d751e6cd296400cd32f72b6c88d1655e61dbc", expand=False, url="https://files.pythonhosted.org/packages/fc/96/e0e863c85d4a467302d064faf0a90c688a8a415f176b698b47b57232bed1/cadquery-2.5.2-py3-none-any.whl")
 
    depends_on("py-setuptools", type="build")
    depends_on("python@3.9:3.11", type=("build", "run"))

    # Core runtime dependencies
    depends_on("py-cadquery-ocp@7.7:", type=("build", "run"))
    depends_on("py-multimethod@1.11:", type=("build", "run"))
    depends_on("py-typish", type=("build", "run"))
    depends_on("py-path", type=("build", "run"))
    depends_on("py-pyparsing", type=("build", "run"))
    depends_on("py-nptyping@2:", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-nlopt@2.9:", type=("build", "run"))
    depends_on("py-casadi@3.6:", type=("build", "run"))
    depends_on("py-ezdxf", type=("build", "run"))

# {'pyparsing': ['1.2.1', '1.2.2', '1.2.4', '1.2.5'], 'cadquery-ocp(<7.8,>=7.7.0a0)': ['2.2.0', '2.3.1'], 'ezdxf': ['2.2.0', '2.2.0b0', '2.2.0b1', '2.2.0b2', '2.3.1', '2.4.0', '2.5.2'], 'multimethod(<2.0,>=1.7)': ['2.2.0', '2.2.0b1', '2.2.0b2', '2.3.1'], 'nlopt': ['2.2.0', '2.2.0b0', '2.2.0b1', '2.2.0b2', '2.3.1', '2.4.0'], 'nptyping(==2.0.1)': ['2.2.0', '2.2.0b1', '2.2.0b2', '2.3.1'], 'typish': ['2.2.0', '2.2.0b0', '2.2.0b1', '2.2.0b2', '2.3.1', '2.4.0', '2.5.2'], 'casadi': ['2.2.0', '2.2.0b0', '2.2.0b1', '2.2.0b2', '2.3.1', '2.4.0', '2.5.2'], 'path': ['2.2.0', '2.2.0b0', '2.2.0b1', '2.2.0b2', '2.3.1', '2.4.0', '2.5.2'], "docutils;extra=='dev'": ['2.2.0', '2.2.0b0', '2.2.0b1', '2.2.0b2', '2.3.0', '2.3.1', '2.4.0'], "ipython;extra=='dev'": ['2.2.0', '2.2.0b0', '2.2.0b1', '2.2.0b2', '2.3.0', '2.3.1', '2.4.0'], "pytest;extra=='dev'": ['2.2.0', '2.2.0b0', '2.2.0b1', '2.2.0b2', '2.3.0', '2.3.1', '2.4.0'], "black(==19.10b0);extra=='dev'": ['2.2.0', '2.2.0b0', '2.2.0b1', '2.2.0b2', '2.3.0', '2.3.1'], "click(==8.0.4);extra=='dev'": ['2.2.0', '2.2.0b0', '2.2.0b1', '2.2.0b2', '2.3.0', '2.3.1'], "ipython;extra=='ipython'": ['2.2.0', '2.2.0b0', '2.2.0b1', '2.2.0b2', '2.3.0', '2.3.1', '2.4.0'], 'cadquery-ocp': ['2.2.0b0', '2.2.0b1'], 'multimethod': ['2.2.0b0'], 'nptyping(>=2)': ['2.2.0b0'], 'cadquery-ocp(<7.7,>=7.6)': ['2.2.0b2'], 'cadquery-ocp<7.8,>=7.7.0a0': ['2.4.0'], 'multimethod==1.9.1': ['2.4.0'], 'nptyping==2.0.1': ['2.4.0'], "black==19.10b0;extra=='dev'": ['2.4.0'], "click==8.0.4;extra=='dev'": ['2.4.0'], 'cadquery-ocp<7.8,>=7.7.0': ['2.5.2'], 'multimethod<2.0,>=1.11': ['2.5.2'], 'nlopt<3.0,>=2.9.0': ['2.5.2'], 'docutils;extra=="dev"': ['2.5.2'], 'ipython;extra=="dev"': ['2.5.2'], 'pytest;extra=="dev"': ['2.5.2'], 'ipython;extra=="ipython"': ['2.5.2']}