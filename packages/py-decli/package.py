# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDecli(PythonPackage):
	"""Minimal, easy-to-use, declarative cli tool"""
	
	homepage = "None"
	pypi = "decli/decli-0.6.2-py3-none-any.whl" 

	version("0.3.0", sha256="3adc2cff147de83f005c96e650cbf6c0ecbe9f1d30fd25622a59059c3d18c0c3", expand=False, url="https://files.pythonhosted.org/packages/6d/09/19b3d53d671e6ae5ccde069ae040d9410a7edac7927107139802d84248c1/decli-0.3.0-py3-none-any.whl")
	version("0.3.1", sha256="6df48ff6c4367ce26c30389d58adfde0f8d5f7769e3ac027f04809ac9f8fb97a", expand=False, url="https://files.pythonhosted.org/packages/5f/06/db14f276d6e4274f91e5f9d5e672e34d873e2f38291601bc4e2fb05119e2/decli-0.3.1-py3-none-any.whl")
	version("0.3.2", sha256="f8a9747aa083e6f5c5ab3e236ebc452727bdadc173bff123a2f2f26b8dd3956e", expand=False, url="https://files.pythonhosted.org/packages/80/87/4c71fad1b30423c0613faf09915e9f296fa4ec0efddea82fae7d033e7905/decli-0.3.2-py3-none-any.whl")
	version("0.4.0", sha256="6da58b9547390ca8014e6ef1353e1bd541be7623057e6eb7ebf439e1d55bdcc4", expand=False, url="https://files.pythonhosted.org/packages/5c/69/2d5cd8abf4b8927aa09efd216c00d52e4d3b96350d1ea9c779e9c1228250/decli-0.4.0-py3-none-any.whl")
	version("0.5.0", sha256="d115345961973dcca812a2100e0f0241bc344f4bcd04a01d0213708d1692e229", expand=False, url="https://files.pythonhosted.org/packages/10/37/afdb88bf00d09daf92989f229bdd8efbefc061d053cef975eac44aaf0c7d/decli-0.5.0-py3-none-any.whl")
	version("0.5.1", sha256="36dbda6cc9fdd7880b7ee141bccab048672307f4f419072aa1a394b01cb10a32", expand=False, url="https://files.pythonhosted.org/packages/35/a2/f2583da64ace2120299f5c115c60412a238b0a321c3446cf1f05c192bb98/decli-0.5.1-py3-none-any.whl")
	version("0.5.2", sha256="d3207bc02d0169bf6ed74ccca09ce62edca0eb25b0ebf8bf4ae3fb8333e15ca0", expand=False, url="https://files.pythonhosted.org/packages/c8/31/70f166640b1571e462b6a86811e8dfa24c2359609dd91ac6b95d93814059/decli-0.5.2-py3-none-any.whl")
	version("0.6.0", sha256="d5ed1d509f5a6cf765a4d7350f7ffb0be0c1770840cbd38b05fb0aab642645e8", expand=False, url="https://files.pythonhosted.org/packages/6c/ef/e43cb1fc03184b14e1851b1dcf8c33bffda2b90ace6fa1414964992757dc/decli-0.6.0-py3-none-any.whl")
	version("0.6.1", sha256="7815ac58617764e1a200d7cadac6315fcaacc24d727d182f9878dd6378ccf869", expand=False, url="https://files.pythonhosted.org/packages/ac/0a/cd94a388fa19a7c512009dc879939591221eae603c1c2ed2e73fa5378961/decli-0.6.1-py3-none-any.whl")
	version("0.6.2", sha256="2fc84106ce9a8f523ed501ca543bdb7e416c064917c12a59ebdc7f311a97b7ed", expand=False, url="https://files.pythonhosted.org/packages/bf/70/3ea48dc9e958d7d66c44c9944809181f1ca79aaef25703c023b5092d34ff/decli-0.6.2-py3-none-any.whl")

	depends_on("python@3.7:", type=("build", "run"))
