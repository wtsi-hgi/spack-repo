# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTbats(PythonPackage):
	"""BATS and TBATS for time series forecasting"""
	
	homepage = "https://github.com/intive-DataScience/tbats"
	pypi = "tbats/tbats-1.1.3-py3-none-any.whl" 

	version("1.0.0", sha256="7c09b9ba19e6631e19277bdcab4fc90c82985491f7e410c635b8eaa6ff2f908b", expand=False, url="https://files.pythonhosted.org/packages/11/a1/2db3e64b4d6d4ae6ef9e1402120be5498c45e8415bdd34e1792f50641924/tbats-1.0.0-py3-none-any.whl")
	version("1.0.1", sha256="d8515716285bc8a5bccfc7b4e818706a5b5fe0e9ff1964966bc2be782ea97cbe", expand=False, url="https://files.pythonhosted.org/packages/c2/3c/7f80ea0781b49e78915fa734c260225bbc5904ce66791836f0d42c003286/tbats-1.0.1-py3-none-any.whl")
	version("1.0.10", sha256="27be211aab53f922e698c90a0fa20633660e86286f97aaacdb544677dd131e92", expand=False, url="https://files.pythonhosted.org/packages/52/a7/44a9058ed3c14f7842ab63aeb95e7c4e157f4e9cf8515ce295e7124f2249/tbats-1.0.10-py3-none-any.whl")
	version("1.0.2", sha256="f58aec83c679ed976a29cbaf62c779f8eaca5c8c11d276044c7798c94e0becff", expand=False, url="https://files.pythonhosted.org/packages/19/88/edd993852b27e4cb3dff526d2c18ab367b0807e78be0ebcc76d350ff4403/tbats-1.0.2-py3-none-any.whl")
	version("1.0.3", sha256="673feabdac5a7afde350ca74e5a6b6ab76bcf07a643d2132cc56bb661353f39e", expand=False, url="https://files.pythonhosted.org/packages/09/02/a7a5a753c0e7abc3f6b3e903f507ca9e85556b2150b1fb78d6a521a4247b/tbats-1.0.3-py3-none-any.whl")
	version("1.0.4", sha256="5d06be7c2e84410ce78e8a0781de01e0fea60d8c9db65cdc9f9f8550c512590d", expand=False, url="https://files.pythonhosted.org/packages/0a/db/e76e3d16dc0b5c0ddd41ead809603124d3eb43444ca913c4bfd83797c84f/tbats-1.0.4-py3-none-any.whl")
	version("1.0.5", sha256="8269d7c4dd50ed6f30f1a61d5715e46ba09f90612dbc7041f4375dd0327d5480", expand=False, url="https://files.pythonhosted.org/packages/4d/66/cf4eac2761f1eeae1cf3e2d6e3a0519a21d1fbf2d79bc9fe1c41b4ee11d9/tbats-1.0.5-py3-none-any.whl")
	version("1.0.6", sha256="7c3f1b0937334cfb9ceaa1179c2ba1bd87b1ef5775f70d6d4f5b24cd39337453", expand=False, url="https://files.pythonhosted.org/packages/b2/63/c40efff2190543cfa80fe0b9eea85f66d7149b1ff236571a8774436218be/tbats-1.0.6-py3-none-any.whl")
	version("1.0.7", sha256="3c6a109016d2fb9688f5708184d9dda332e906cca35dc31415779995f264d273", expand=False, url="https://files.pythonhosted.org/packages/e2/22/c8e024d013e75dc23ded89c5d6f3364211f54cd13701d987ace6ce1133a5/tbats-1.0.7-py3-none-any.whl")
	version("1.0.8", sha256="1f006daa231503bbf72bf2183734925fec713fce913bd1e0c7878be1f4812405", expand=False, url="https://files.pythonhosted.org/packages/66/45/9766fec668f0197e0e4fa0a7b52330ccf907af622e8237724cb539b44171/tbats-1.0.8-py3-none-any.whl")
	version("1.0.9", sha256="32334d146291886f285aefe1ca1620b6fa6a1068a9ac6e58760cdee31f901eb1", expand=False, url="https://files.pythonhosted.org/packages/5e/f2/04545b598030cd72807847d9230a5db619658be3a650e112ed18acb3a122/tbats-1.0.9-py3-none-any.whl")
	version("1.1.0", sha256="dfda4a68e0642558679f46e3cbb7c14df08760d009f709d9d9dff6bb35b33191", expand=False, url="https://files.pythonhosted.org/packages/7d/34/c376a23348993deb50d36372324f4e7c5510608a1f49bca7d20390824327/tbats-1.1.0-py3-none-any.whl")
	version("1.1.1", sha256="7c7360c62c8eadedc0536e8341e23e9af534bb797f2f4e3d051e79284ce3cc3d", expand=False, url="https://files.pythonhosted.org/packages/1d/d1/f5d878133d9167f03fd3eeb814b6a298132d76776582e2482a402b4d0186/tbats-1.1.1-py3-none-any.whl")
	version("1.1.2", sha256="e7638f7fcb4c98db9f51432afd5abaac790b887519ca351c57841946f72e7fe6", expand=False, url="https://files.pythonhosted.org/packages/30/71/7a75656e705070ef84f12fac79d2596badb9254f9c3ea8be24e872fa1dfa/tbats-1.1.2-py3-none-any.whl")
	version("1.1.3", sha256="aff37f39115583028dacbd87227bc2ac65e696ea25543ddcd78e334e1fbe8e3a", expand=False, url="https://files.pythonhosted.org/packages/63/94/1949dc644c3fa05b736b988dc8058122f8c0187778ff9f18070bce2d4ddd/tbats-1.1.3-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-pmdarima", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))

# {'numpy': ['1.0.0', '1.0.1', '1.0.10', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.0.6', '1.0.7', '1.0.8', '1.0.9', '1.1.0', '1.1.1', '1.1.2', '1.1.3'], 'scipy': ['1.0.0', '1.0.1', '1.0.10', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.0.6', '1.0.7', '1.0.8', '1.0.9', '1.1.0', '1.1.1', '1.1.2', '1.1.3'], 'pmdarima': ['1.0.0', '1.0.1', '1.0.10', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.0.6', '1.0.7', '1.0.8', '1.0.9', '1.1.0', '1.1.1', '1.1.2', '1.1.3'], 'sklearn': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.0.6', '1.0.7'], "pip-tools;extra=='dev'": ['1.0.0', '1.0.1', '1.0.10', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.0.6', '1.0.7', '1.0.8', '1.0.9', '1.1.0', '1.1.1', '1.1.2', '1.1.3'], "rpy2;extra=='dev'": ['1.0.0', '1.0.1', '1.0.10', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.0.6', '1.0.7', '1.0.8', '1.0.9', '1.1.0', '1.1.1', '1.1.2', '1.1.3'], 'scikit-learn': ['1.0.10', '1.0.8', '1.0.9', '1.1.0', '1.1.1', '1.1.2', '1.1.3'], "pytest;extra=='dev'": ['1.1.1', '1.1.2', '1.1.3']}