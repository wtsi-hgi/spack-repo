# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMygene(PythonPackage):
	"""Python Client for MyGene.Info services."""
	
	homepage = "https://github.com/biothings/mygene.py"
	pypi = "mygene/mygene-3.2.2-py2.py3-none-any.whl" 

	version("0.1.0", sha256="da9d44b738f35b6a1627c068d4655c3c936152ad2f79a3348be04abbdc907c61")
	version("1.0.0", sha256="185e7ce91c8485258769b986d6cfb9e45e5cfa7ff2b817ffefb4b1c61ea4ff2d")
	version("2.0.0", sha256="9524be743c6807d39670cb1237c5d67fc102c53e932652cc058cc8137e48327c")
	version("2.0.1", sha256="4d23e03e57779767535e5d78b5145da3bd4c86e161b1b7dc1a24b71705f7051c")
	version("2.1.0", sha256="107f931f18e15a55cd72b0498de83be09103b63629382fbd27831abcd44de5d2")
	version("2.2.0", sha256="dcd1d9de9c9743c4e30471808c51db4b3d621e4a43ec1e8d8116abec7344694e")
	version("2.3.0", sha256="8ee8274c1483970179972d2e893035a1fc4877a86abc5e096c19cae2dc851f28", expand=False, url="https://files.pythonhosted.org/packages/a8/3d/aa55b83f940b59b625c0f4df6f59acd8d6397800ec3d99ac920f9d4a0568/mygene-2.3.0-py2.py3-none-any.whl")
	version("3.0.0", sha256="20c74296fd8fea96bbf498fba8190a11f7838fdd9d1009d7089f399310d09edf", expand=False, url="https://files.pythonhosted.org/packages/16/ef/67ae813d239505424cc8c77823aa1a9677a9d80b9ab62da94581a49ecae6/mygene-3.0.0-py2.py3-none-any.whl")
	version("3.1.0", sha256="0baa2d84748b54b951c773d9af34a149befb598c57c6cf36d910e82fead17e21", expand=False, url="https://files.pythonhosted.org/packages/10/30/596b5e4077c46add8782de6ac54c173d10b8f15db5bf57d6d8538565c468/mygene-3.1.0-py2.py3-none-any.whl")
	version("3.2.0", sha256="1acf67b22444be10c78a27531357d128b802662a748c480f4880cd9872e0c8fa", expand=False, url="https://files.pythonhosted.org/packages/80/a4/4e783c372244d21e1d94e9d1acdb6c66863a9a7cc67066d16c867583cbe0/mygene-3.2.0-py2.py3-none-any.whl")
	version("3.2.1", sha256="3e2f067e631433e829626ef6cee9754d7fc5a591cb6a5c6023f40fa22fbe5927", expand=False, url="https://files.pythonhosted.org/packages/1c/4e/efae7b0e2b27c725921acda52e3f3ee7b0c9bd8849b2bb1ae02554cc6a62/mygene-3.2.1-py2.py3-none-any.whl")
	version("3.2.2", sha256="18d85d1b28ecee2be31d844607fb0c5f7d7c58573278432df819ee2a5e88fe46", expand=False, url="https://files.pythonhosted.org/packages/a7/b7/132b1673c0ec00881d49d56c09624942fa0ebd2fc21d73d80647efa082e9/mygene-3.2.2-py2.py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-biothings-client", type=("build", "run"))

# {'requests(>=2.3.0)': ['2.3.0', '3.0.0'], 'biothings-client(>=0.2.0)': ['3.1.0'], 'biothings-client(>=0.2.4)': ['3.2.0'], 'biothings-client(>=0.2.5)': ['3.2.1'], 'biothings-client(>=0.2.6)': ['3.2.2']}