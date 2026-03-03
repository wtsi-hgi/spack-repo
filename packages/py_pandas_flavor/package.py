# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPandasFlavor(PythonPackage):
	"""The easy way to write your own Pandas flavor."""
	
	homepage = "https://github.com/Zsailer/pandas_flavor"
	pypi = "pandas-flavor/pandas_flavor-0.6.0-py3-none-any.whl" 

	version("0.1.0", sha256="4af19e9937c7b2aab89b1bf717dad90151f6d9dd9e5da4e03c0fa377001ac294", expand=False, url="https://files.pythonhosted.org/packages/b4/61/8d9f0e693a6177223ca67514f783e9c1a2f8fe48892349b94e34a18b3a6c/pandas_flavor-0.1.0-py2.py3-none-any.whl")
	version("0.1.1", sha256="5ae12ca81813baad0821ecd7316d89575cefac5a00e9e0993d4c337e10dd67f6", expand=False, url="https://files.pythonhosted.org/packages/e1/c3/c9cceafff3247ba7442395f106087e3867d9f741e4fbfb19d77178904a4e/pandas_flavor-0.1.1-py2.py3-none-any.whl")
	version("0.1.2", sha256="1838b4f63b676715d39f9abf39ad281b5f6d655fceebf8142090852f1e72e25e", expand=False, url="https://files.pythonhosted.org/packages/79/35/092aa4518f4b386eb557c634f9765cdb3c6350950dfe2c58ed6e088e805d/pandas_flavor-0.1.2-py2.py3-none-any.whl")
	version("0.2.0", sha256="ce4d3640a89435c27eb2369305455865f043464ee5ae450e5388f4fb30eae241", expand=False, url="https://files.pythonhosted.org/packages/9a/57/7fbcff4c0961ed190ac5fcb0bd8194152ee1ee6487edf64fdbae16e2bc4b/pandas_flavor-0.2.0-py2.py3-none-any.whl")
	version("0.3.0", sha256="af968da59cbc204c5a7c596b2a454e72b081494439dec3364f830792cf2f97b8", expand=False, url="https://files.pythonhosted.org/packages/1b/83/086c0c5b96f3e6ba637ce08156420eddc1194e711fab934bdfe37e1ac0d7/pandas_flavor-0.3.0-py3-none-any.whl")
	version("0.5.0", sha256="2d9aef3ff13b6679ded9b944c457493820b2afce22d4029b7f36457710df8679", expand=False, url="https://files.pythonhosted.org/packages/0e/b1/2752e080b23c8018593ff41b1bfe1c24ef7ef46641003c2e5e3fc7a27bf0/pandas_flavor-0.5.0-py3-none-any.whl")
	version("0.6.0", sha256="a32c9e2e0da702579320cf2bd0078cee91807713bc9c65ff522f6b0289899893", expand=False, url="https://files.pythonhosted.org/packages/67/1a/bfb5574b215f530c7ac5be684f33d60b299abbebd763c203aa31755f2fb2/pandas_flavor-0.6.0-py3-none-any.whl")

	depends_on("py-xarray", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))

# {'pandas': ['0.1.0', '0.1.1', '0.1.2', '0.2.0'], 'xarray': ['0.2.0', '0.3.0', '0.5.0', '0.6.0'], 'pandas(>=0.23)': ['0.3.0', '0.5.0', '0.6.0'], 'lazy-loader(==0.1rc2)': ['0.3.0'], 'lazy-loader(>=0.1)': ['0.5.0']}