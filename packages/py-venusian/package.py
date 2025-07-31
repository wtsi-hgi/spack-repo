# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyVenusian(PythonPackage):
	"""A library for deferring decorator actions"""
	
	homepage = "https://pylonsproject.org/"
	pypi = "venusian/venusian-3.1.1-py3-none-any.whl" 

	version("0.1", sha256="b7c59aaf2bd0fd6364e083cb80a097b4fa9f80219643feefc5382006d6343ebf")
	version("0.2", sha256="07f079fe778d331bf53f6c3ae14f15cbb65cf0fce94862161cc54d4e4a4aea2e")
	version("0.3", sha256="6425956f4e8620e4a9e1bea0a4974f21e4338824b863ab352242c090ba757255")
	version("0.4", sha256="d0ff8498bb034f066a5623e95ed1d75882c919868139016ff30836bc05a426a1")
	version("0.5", sha256="81a11a9cbd8bb0266b04c153d3fb1cb9d821b48dbcd633274087604a6ec811d7")
	version("0.6", sha256="10aaf0c2ad63e0b61c7402e288a1cde7e289637e2607dfc282497b03816d4ded")
	version("0.7", sha256="4ed59589c3bbda7d848c78ec0297dd82933c84123f7b0e4eab2c311ab26e997b")
	version("0.8", sha256="62e035e0556d600de1055c33675cfdb0dbfc7047439be065d75deaf23226380f")
	version("0.9", sha256="d0e887f1434b0ae204236b023b67685ce6e1448eb37bff271e6419c2076848b2")
	version("1.0", sha256="1720cff2ca9c369c840c1d685a7c7a21da1afa687bfe62edd93cae4bf429ca5a")
	version("1.0a1", sha256="b2090ed620788c25dcc1d2f2457e767aa28ea26cb4943803014543c425fb62f9")
	version("1.0a2", sha256="48772b136311aa1b0f0c40b664d180018ca448125fc3dc9f82d2275b61289d28")
	version("1.0a3", sha256="47fb92f6565441e9b0d55e07d9990194f79088de16cadadd01ae1c7d1f2e586a")
	version("1.0a4", sha256="6bb87b48f4bb8cb856c267c59408c43f372f30611e567b5ec69e9cecd9b67d8a")
	version("1.0a5", sha256="f968aadc195b62c75449b38fc8afaf7def1a9fa0cea20027b8a8bf9d694450d8")
	version("1.0a6", sha256="6b9a14a6d903fa6074d4bc221e603d548399fd1c48b37a036694828786516d86")
	version("1.0a7", sha256="adba7aa463569f7483186e74a2c0a7ea239879376d24066e52b71fc227dcede6")
	version("1.0a8", sha256="a1b054d4ccf0859a76d900c49f419645279298d5316be3a65a1c00a40719bce0")
	version("1.1.0", sha256="757162c5f907e18571b6ab41b7673e5bf18cc8715abf8164292eaef4f1610668", expand=False, url="https://files.pythonhosted.org/packages/2f/c2/3d122e19287ed7d73f03821cef87e53673f27d41cae54ee3a46e92b147e2/venusian-1.1.0-py2.py3-none-any.whl")
	version("1.2.0", sha256="2f2d077a1eedc3fda40425f65687c8c494da7e83d7c23bc2c4d1a40eb3ca5b6d", expand=False, url="https://files.pythonhosted.org/packages/21/80/8e2ac4aef69e927754277d29636b65eceb4767e9da90a2c3046c4176184a/venusian-1.2.0-py2.py3-none-any.whl")
	version("2.1.0", sha256="f3efaf52b0984d2d238417e4a6dfac0fa3f0dc2f69d17d6a810f6428efc3ff3c", expand=False, url="https://files.pythonhosted.org/packages/72/46/ffe45f3b4a99309387551f4a06ed7e6c06fb163226e63b09aa5d6a21a280/venusian-2.1.0-py2.py3-none-any.whl")
	version("3.0.0", sha256="06e7385786ad3a15c70740b2af8d30dfb063a946a851dcb4159f9e2a2302578f", expand=False, url="https://files.pythonhosted.org/packages/43/92/3d522a710867168ee422a0ffbd712c425ece937aaeec4381497a59e24faf/venusian-3.0.0-py3-none-any.whl")
	version("3.1.0", sha256="d1fb1e49927f42573f6c9b7c4fcf61c892af8fdcaa2314daa01d9a560b23488d", expand=False, url="https://files.pythonhosted.org/packages/2c/d7/36860f68eb977ad685d0f0fda733eca913dbda1bb29bbc5f1c5ba460201a/venusian-3.1.0-py3-none-any.whl")
	version("3.1.1", sha256="0845808a985976acbceaa1fbb871c7fac4fb28ae75453232970e9c2c2866dbf4", expand=False, url="https://files.pythonhosted.org/packages/5a/4b/34d926eba40db81b204066a60b4efdc5d8867a8efcbfe44d69b634b1c907/venusian-3.1.1-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.7:", type=("build", "run"))

# {"Sphinx;extra=='docs'": ['1.1.0', '1.2.0', '2.1.0', '3.0.0'], "repoze.sphinx.autointerface;extra=='docs'": ['1.1.0', '1.2.0', '2.1.0', '3.0.0', '3.1.0'], "coverage;extra=='testing'": ['1.1.0', '1.2.0', '2.1.0', '3.0.0', '3.1.0'], "pytest;extra=='testing'": ['1.1.0', '1.2.0', '2.1.0', '3.0.0', '3.1.0'], "pytest-cov;extra=='testing'": ['1.1.0', '1.2.0', '2.1.0', '3.0.0', '3.1.0'], "Sphinx>=4.3.2;extra=='docs'": ['3.1.0'], "pylons-sphinx-themes;extra=='docs'": ['3.1.0'], "sphinx-copybutton;extra=='docs'": ['3.1.0'], 'pytest;extra=="testing"': ['3.1.1'], 'pytest-cov;extra=="testing"': ['3.1.1'], 'coverage;extra=="testing"': ['3.1.1'], 'Sphinx>=4.3.2;extra=="docs"': ['3.1.1'], 'repoze.sphinx.autointerface;extra=="docs"': ['3.1.1'], 'pylons-sphinx-themes;extra=="docs"': ['3.1.1'], 'sphinx-copybutton;extra=="docs"': ['3.1.1']}