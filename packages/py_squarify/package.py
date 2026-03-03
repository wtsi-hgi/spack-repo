# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySquarify(PythonPackage):
	"""Pure Python implementation of the squarify treemap layout algorithm"""
	
	homepage = "https://github.com/laserson/squarify"
	pypi = "squarify/squarify-0.4.4-py3-none-any.whl" 

	version("0.1", sha256="4a469f53f778fbae03f8b2eac561fda28d4c79a1095718469fd2227cff9538ea")
	version("0.1.1", sha256="cc196c9d6b0d65d2e99ca0760619cb846bef30867054b64a6b5ebb6192ba11c2")
	version("0.1.2", sha256="79fb4ea98790ddaec57f4eb44a5fdbbd82fce7fdd86a57385a26bc62bfdf74fe")
	version("0.1.3", sha256="d897764011f2b3fd9e3a1b7980831f0c5960f6336e5b9c2dd3616aa29e4d738d")
	version("0.2.0", sha256="580b683f53359b751b83f99f84df7dd96c1b13b8334839db5378ba0dfd6ff4a3")
	version("0.3.0", sha256="bcb06fb2706975e42426149b45dda64dde6a1abefc384caec9ba245914cc42bc", expand=False, url="https://files.pythonhosted.org/packages/c5/76/80933fa481c630a3295d47b026b704094080efb7938edf8ab9e1b0c0e5ba/squarify-0.3.0-py3-none-any.whl")
	version("0.4.0", sha256="a411ec40927c01170bed5d19cb36cd81a57f07c5d4c7d7b51742464e03c7d135", expand=False, url="https://files.pythonhosted.org/packages/b4/36/145055625142c00058106438a3ea87d23989304d1044c204aff3c226274b/squarify-0.4.0-py3-none-any.whl")
	version("0.4.1", sha256="16807f0459073ba0075e394cd0a91fb85c5769bcb982ac8100c667adcbb1fe03", expand=False, url="https://files.pythonhosted.org/packages/41/71/eb81eb81805a8a4fda00b0e288c0734bc848603542c72774ab5f0d0633ee/squarify-0.4.1-py3-none-any.whl")
	version("0.4.2", sha256="fad85ef09aba06aa7f35f7af87c8d1318508223708b121c0aff1dbf09530708d", expand=False, url="https://files.pythonhosted.org/packages/4e/f2/1f47d7f8c34e3c5f45de8b7fad06947558964e05ce6cccc94cf2066bd22b/squarify-0.4.2-py3-none-any.whl")
	version("0.4.3", sha256="bec7011e0c7f4103fe57a1c16a7c091d9dc1be0f23d774e1c568b748a6f818f6", expand=False, url="https://files.pythonhosted.org/packages/0b/2b/2e77c35326efec19819cd1d729540d4d235e6c2a3f37658288a363a67da5/squarify-0.4.3-py3-none-any.whl")
	version("0.4.4", sha256="d7597724e29d48aa14fd2f551060d6b09e1f0a67e4cd3ea329fe03b4c9a56f11", expand=False, url="https://files.pythonhosted.org/packages/b7/3c/eedbe9fb07cc20fd9a8423da14b03bc270d0570b3ba9174a4497156a2152/squarify-0.4.4-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
