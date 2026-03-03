# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyXdgBaseDirs(PythonPackage):
	"""Variables defined by the XDG Base Directory Specification"""
	
	homepage = "https://github.com/srstevenson/xdg-base-dirs"
	pypi = "xdg-base-dirs/xdg_base_dirs-6.0.2-py3-none-any.whl" 

	version("6.0.0", sha256="71b878d3b6c80923a8ddd7c4fb25f9f694c6796aa79214c3fe32dd49a13dcc82", expand=False, url="https://files.pythonhosted.org/packages/f7/1b/8f9beeb6df73bfc0e05e16dcbdc23c22ef8ec3b156b36fcc664891c69876/xdg_base_dirs-6.0.0-py3-none-any.whl")
	version("6.0.1", sha256="63f6ebc1721ced2e86c340856e004ef829501a30a37e17079c52cfaf0e1741b9", expand=False, url="https://files.pythonhosted.org/packages/94/e0/8c5ae4c8fc31492de9db4c6013f28811c0ad3fbfad57b4220fe75a312243/xdg_base_dirs-6.0.1-py3-none-any.whl")
	version("6.0.2", sha256="3c01d1b758ed4ace150ac960ac0bd13ce4542b9e2cdf01312dcda5012cfebabe", expand=False, url="https://files.pythonhosted.org/packages/fc/03/030b47fd46b60fc87af548e57ff59c2ca84b2a1dadbe721bb0ce33896b2e/xdg_base_dirs-6.0.2-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.10:4.0", type=("build", "run"))
