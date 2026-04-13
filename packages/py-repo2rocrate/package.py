# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRepo2rocrate(PythonPackage):
	"""Generate RO-Crates from workflow repositories"""
	
	homepage = "https://github.com/crs4/repo2rocrate"
	pypi = "repo2rocrate/repo2rocrate-0.1.2-py3-none-any.whl" 

	version("0.1.2", sha256="aae2d7923eef11896aabcf676f74460dfff35060c71996778dc62fd3af199d4d", expand=False, url="https://files.pythonhosted.org/packages/df/b1/2175cddf0aabb2c66545178c4c48443da1b36e1f8f213da481003707e531/repo2rocrate-0.1.2-py3-none-any.whl")
	version("0.1.1", sha256="6c743f03c1f84e606a732c4ece07fba63a3038e10172edd93a2dc33e999b5bce", expand=False, url="https://files.pythonhosted.org/packages/05/91/01731df41f957458ef9ba8e4d3fad13a2fb9271134b5a3b9715034739c4f/repo2rocrate-0.1.1-py3-none-any.whl")
	version("0.1.0", sha256="b05eec7eb1c37a8dc9a24010551b4a2c5b038065a3ac7c1f2dfbf53202e93bb3", expand=False, url="https://files.pythonhosted.org/packages/c7/fa/d9eb792ffe5f729492ff3ae0473a79ed1377c39a937b4cfa939bf4384d8b/repo2rocrate-0.1.0-py3-none-any.whl")

	depends_on("python@3.6:", type=("build", "run"))
	depends_on("py-pyyaml", type=("build", "run"))
	depends_on("py-click", type=("build", "run"))
	depends_on("py-rocrate", type=("build", "run"))
