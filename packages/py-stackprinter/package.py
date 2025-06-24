# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyStackprinter(PythonPackage):
	"""Debug-friendly stack traces, with variable values and semantic highlighting"""
	
	homepage = "https://github.com/cknd/stackprinter"
	pypi = "stackprinter/stackprinter-0.2.9-py3-none-any.whl" 

	version("0.1", sha256="71192949afd6e9f7bf806f1e037706a95de8cb51483d4be93c7077cf7de2d27a", expand=False, url="https://files.pythonhosted.org/packages/7a/b3/8124101b1359e3fb852194260c8dedf08958cd88370e8ec9b296a9901e14/stackprinter-0.1-py3-none-any.whl")
	version("0.1.1", sha256="f3f53d1db8015d8d2f10c1d3f3c1b0b9926a253d85ecda53995967c79d7aa1c5", expand=False, url="https://files.pythonhosted.org/packages/07/c1/e92714a3d9283f96899cee3a238c52b20688985cea7915cb74549d34e595/stackprinter-0.1.1-py3-none-any.whl")
	version("0.1.1.post1", sha256="3fd305ce99b48d86f883a050be3c4b71a5459ba37a842bafe20e480627c05216", expand=False, url="https://files.pythonhosted.org/packages/34/9a/e1cde52afa38b90a29fa738f80f06cbbb2bb8303e5f754d427aae8b1aea5/stackprinter-0.1.1.post1-py3-none-any.whl")
	version("0.1.2", sha256="586ee6edc66358404f17b65e8b66fb635101f972a10fd81ad0ecc76d4b44f2c7", expand=False, url="https://files.pythonhosted.org/packages/8a/d0/c3c4ef5de20224c388742d1ce7723851eee6f1d13624e9ca9d3a90013643/stackprinter-0.1.2-py3-none-any.whl")
	version("0.1.3", sha256="90345a7ad11dc5ed9cbc42b535abd5e56a93c19a9ed8f56e891ec9b92de82849", expand=False, url="https://files.pythonhosted.org/packages/b3/bd/724de5d7412f38c30fa2f567e6365496f0cc28656679e53b9625a5d15b2d/stackprinter-0.1.3-py3-none-any.whl")
	version("0.1.4", sha256="9ee8bf2213b8df3d44935f164db00e57dee6a8f3b4a28e149ced76330ff56469", expand=False, url="https://files.pythonhosted.org/packages/5b/a6/3517a73a6e58d27d4f877b22696456719d1958b68343a5815f364ff5a492/stackprinter-0.1.4-py3-none-any.whl")
	version("0.1.5", sha256="3a5bd9c5e427430c8c2ffc4f2e4d5d254f624c77ede49a497ab6b4f151a2bb68", expand=False, url="https://files.pythonhosted.org/packages/76/ff/e0f3ebad0c7ffa89856ba0065f31f47e0ffb936a59faa53799f45547df58/stackprinter-0.1.5-py3-none-any.whl")
	version("0.1.6", sha256="8b4e2b879b510f2af560de13899437fdf090eefa543958ef793f918817268064", expand=False, url="https://files.pythonhosted.org/packages/b4/50/86afcf78be53ff71493648c0725ba7916bdb7aa74a844f48c52d40e7ea47/stackprinter-0.1.6-py3-none-any.whl")
	version("0.2.0", sha256="d6f7928c1e5239cd23b5b21c63029596edbf82332d53fb1ddcd6e5d949764cf9", expand=False, url="https://files.pythonhosted.org/packages/64/ad/97599287c2ab993328adef81df2755f9d41804d52f8a25f2df623a919427/stackprinter-0.2.0-py3-none-any.whl")
	version("0.2.1", sha256="9028d181b88936ed7a5be0edee1291235a16ef9791824fb6c69eba0fc13287bc", expand=False, url="https://files.pythonhosted.org/packages/7e/69/de6b9612c4d8ded14b98d9fff957be2e3121edd6d94e0f8d1a12199f30c4/stackprinter-0.2.1-py3-none-any.whl")
	version("0.2.10", sha256="496e6cd058e7dd6f41e0c67e044f79a894297bec9fb80493a4fd094fac1e4677", expand=False, url="https://files.pythonhosted.org/packages/1d/08/2d7fcd2d98d01f7cbdf0a9992635b771758f76cbe52fd9aaa1119db5aae5/stackprinter-0.2.10-py3-none-any.whl")
	version("0.2.11", sha256="101da55db7dfd54af516e3e209db9c84645285e5ea00d0b0709418dde2f157a1", expand=False, url="https://files.pythonhosted.org/packages/cf/90/289ff876c950e6fe2cd58f6ec7da36cd83791c038b6263dc22bceb6836cc/stackprinter-0.2.11-py3-none-any.whl")
	version("0.2.12", sha256="0a0623d46a5babd7a8a9787f605f4dd4a42d6ff7aee140541d5e9291a506e8d9", expand=False, url="https://files.pythonhosted.org/packages/7c/15/485186e37a06d28b7fc9020ad57ba1e3778ee9e8930ff6c9ea350946ffe1/stackprinter-0.2.12-py3-none-any.whl")
	version("0.2.2", sha256="2398cdb54b3d9edfffed9518cb83d0af8ef43f62c34c792e493a09f2be2b1612", expand=False, url="https://files.pythonhosted.org/packages/63/78/5eebf787ab91820f248717154de99186195517cd1726ece990a593a1915b/stackprinter-0.2.2-py3-none-any.whl")
	version("0.2.3", sha256="a21590e1c8fc4aad1e97e89df2bcf86dcaf55f47b1bbb4dfd209361d28fd9d68", expand=False, url="https://files.pythonhosted.org/packages/3e/35/996a248820825e1081267d17ea1ca2d089e4f3bbe509c91e8503437c1260/stackprinter-0.2.3-py3-none-any.whl")
	version("0.2.4", sha256="d181cdd2bfc29b464926c5be77eb9aa6e58031cac98b07b8d513c6e6eeeb2fab", expand=False, url="https://files.pythonhosted.org/packages/84/64/4e613b325887812300160ae6e6a5b3dfe3b49dbd7e2533e11099f28e1de7/stackprinter-0.2.4-py3-none-any.whl")
	version("0.2.5", sha256="e6770d1f932992caa37f1c734ca40429ee7358163ec7f262dcd3c8371b260006", expand=False, url="https://files.pythonhosted.org/packages/f3/f5/ff972ffa3b54afce3f48d36bf749e3048ee22473afa4489dd6c5c1be402a/stackprinter-0.2.5-py3-none-any.whl")
	version("0.2.6", sha256="163d7620ef8afab7c5e79c533ec1a424b15c6737faeef592b51846a35926bd82", expand=False, url="https://files.pythonhosted.org/packages/e8/cb/32869bad18b621815f335930eb2f719ab91ac7f24478c30bda7e86b750ca/stackprinter-0.2.6-py3-none-any.whl")
	version("0.2.7", sha256="4d366e092751399e266211d010e3f11d3f9a3416e9a2e118994d7bc62c1de0ca", expand=False, url="https://files.pythonhosted.org/packages/2d/76/81771ca0bb71bc8ff3d1afa14412a422632ca557fbd7a0ffa235b6adc6d7/stackprinter-0.2.7-py3-none-any.whl")
	version("0.2.8", sha256="005f7c8f9fce58259e9853c93534bb6623a40b0ce80fbfa0d15774a1c5f193b9", expand=False, url="https://files.pythonhosted.org/packages/c5/26/d0076d4d49834621170f457a2667e3ed1540bac3e73b7ce269238e6be482/stackprinter-0.2.8-py3-none-any.whl")
	version("0.2.9", sha256="87c0357100da3cf3ec0bb71ac6e374b5d970856d644815277987ff4a5d5d0530", expand=False, url="https://files.pythonhosted.org/packages/83/5f/0c3e783d5cbf11ecffd41b4c170f5b909c525c3572d06f88ca5ad0ff45fd/stackprinter-0.2.9-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.4:", type=("build", "run"))
