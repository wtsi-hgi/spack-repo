# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyVaexJupyter(PythonPackage):
	"""Jupyter notebook and Jupyter lab support for vaex"""
	
	homepage = "https://www.github.com/maartenbreddels/vaex"
	pypi = "vaex-jupyter/vaex_jupyter-0.8.2-py3-none-any.whl" 

	version("0.1.0", sha256="cf5b22c8302c733e0803c6b668a08e5adf119134e7c1f8c703203ce18cbeaef8")
	version("0.1.1", sha256="7a9720b0115ea29f9c2f909ace253d72472af75f363155639dc7e53e46430aa6")
	version("0.2.0", sha256="c878797ea166adcd001ec41b2898fe8648c522d62cbd93c319ef5987c8e63ac2")
	version("0.2.1", sha256="c0e982a791744b8bd6fa11a7aa33ae31251281663aaa34ff05b9aad87dd17ebc")
	version("0.2.2", sha256="dd634baeb598ef878e2022ca5cf96d9e32832dda44c902724699b4e7c06b27aa")
	version("0.2.3", sha256="a17507bc47cd098252902d041f2bddf09c6a5a26360dcc391ec9b504915fcccf")
	version("0.3.0", sha256="a1648488cdcc7e3e896cba5c74d63680b1bdf15521b8824ad4ed8c4c75474288")
	version("0.3.1", sha256="84a294263b9640f7055a6b3fe3ed2051eceaf3c5a51086e72efc30774de85c31")
	version("0.3.2", sha256="4df1a7904bae24f3ea96e5edd8493ecece6f3eea7db6d988f16309bddeff18e6")
	version("0.4.0", sha256="e3c6a21a347f436dcf16ec14f7248215667f614cb2bcf6cdad153708ced4114f")
	version("0.4.1", sha256="338899d17b2ac5134895e17a2691bbca83b343ed3a56b7facad34c2286097184")
	version("0.5.0", sha256="2c4038efceed5357f0c45d2d9cdfa0bf282970e5d6c4efbb8fe0e11d8e5945da", expand=False, url="https://files.pythonhosted.org/packages/9a/03/579c4bdfe39d1bcacca44dfc01ee0f7cd37a97f64899b3fc6a078aa2105b/vaex_jupyter-0.5.0-py3-none-any.whl")
	version("0.5.0a1", sha256="24f0bc761d4fcfa9403c1b5e358e203edfe69339f33a2cbb7b6e47b754bb5d92", expand=False, url="https://files.pythonhosted.org/packages/65/c9/cee4d3807ea58e04c1dbc0a121088f0e6c8af20cd9dcfbaf1ceb1dd3a4f7/vaex_jupyter-0.5.0a1-py3-none-any.whl")
	version("0.5.0a2", sha256="a0e87ed4f39f34aed92422e07f38721c1228ecd885760b6a04f813c6f723d051", expand=False, url="https://files.pythonhosted.org/packages/05/73/bb9ef8ddbd781e2e563b7a8caedf4b9ba392e7004e7c214259ce319f13d3/vaex_jupyter-0.5.0a2-py3-none-any.whl")
	version("0.5.1", sha256="6eca04f24a626a0de4e9a026f1b4b89091cff78de53e14a2274ab90e1a41814f", expand=False, url="https://files.pythonhosted.org/packages/72/1b/9b12b6ac05dafbf785e1cc02afb2a83fefe8c04806f6cde2b3178268036c/vaex_jupyter-0.5.1-py3-none-any.whl")
	version("0.5.1.post0", sha256="485d9a9b4d407bc76b7accb6434f211434c1bd97e38e0f9b5650e751e354e23b", expand=False, url="https://files.pythonhosted.org/packages/ff/a9/d597f31de9fd49a15d6775fe7fb241275be5cd17485c1b12c1d127f719db/vaex_jupyter-0.5.1.post0-py3-none-any.whl")
	version("0.5.2", sha256="4d14759a133260370e6242fb67b72e853999527e649fe321b1944fe007e4f9a7", expand=False, url="https://files.pythonhosted.org/packages/0f/b2/f35480f0091e8ef63cb9561653148c580677c2de04b33b759ef67da5f064/vaex_jupyter-0.5.2-py3-none-any.whl")
	version("0.6.0", sha256="6b614bd0b4ae1ba36ddb06af9df18094c07340bad17fffdfca5ce436e6675590", expand=False, url="https://files.pythonhosted.org/packages/bd/27/de079e129baf62002d3a28216449cc0f26f8750c5778d2285a06c8390488/vaex_jupyter-0.6.0-py3-none-any.whl")
	version("0.6.0.dev1", sha256="734f81eab0d80b244c42f347392a1eef2c54272c3d2f2d9b25ec4a54d9370bc8", expand=False, url="https://files.pythonhosted.org/packages/94/1a/7024d7ae8dbe592f022c74009947b318b02e43249274ac29e6c7c690293a/vaex_jupyter-0.6.0.dev1-py3-none-any.whl")
	version("0.7.0", sha256="935d72b2851598e5b0ee6a4fb25af557a4ecadc8ac8af55c46f799cc182a8670", expand=False, url="https://files.pythonhosted.org/packages/ec/e4/1cd68d9fe57ced34ee80f8ce27e1caae29ab7a900239d27922030e400977/vaex_jupyter-0.7.0-py3-none-any.whl")
	version("0.8.0", sha256="70548740091cf00b650a717cc4167f8443dcf236aa671e0c37ca04e13c1aa40d", expand=False, url="https://files.pythonhosted.org/packages/1f/e3/90616cb8f24fc1ace79b8f9c10b2b16790927a9c7025b541a231dd83345a/vaex_jupyter-0.8.0-py3-none-any.whl")
	version("0.8.1", sha256="cde22042d054cdb27e6d268fc217150b1ea235c7ec0caf306313eea9ae3c05c7", expand=False, url="https://files.pythonhosted.org/packages/ba/8e/ead143246c4016c8df3818fb7f1e1b7248af2d0a70316895905175a7e2fc/vaex_jupyter-0.8.1-py3-none-any.whl")
	version("0.8.2", sha256="5bce62fe1b9da18ce9848ba6c06639e89119c55cbc63e7faf6f025b91564271a", expand=False, url="https://files.pythonhosted.org/packages/90/52/1111c4d6794da4a7d02bf0de4a8424a6c44805bd9dfa14eebdf8fc526685/vaex_jupyter-0.8.2-py3-none-any.whl")

	depends_on("py-xarray", type=("build", "run"))
	depends_on("py-ipyvuetify", type=("build", "run"))
	depends_on("py-ipympl", type=("build", "run"))
	depends_on("py-ipyleaflet", type=("build", "run"))
	depends_on("py-ipyvolume", type=("build", "run"))
	depends_on("py-bqplot", type=("build", "run"))
	depends_on("py-vaex-viz", type=("build", "run"))
	depends_on("py-vaex-core", type=("build", "run"))
