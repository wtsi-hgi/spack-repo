# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHydride(PythonPackage):
	"""Adding hydrogen atoms to molecular models"""
	
	homepage = "https://hydride.biotite-python.org"
	pypi = "hydride/hydride-1.2.3.tar.gz" 

	version("0.1.0", sha256="a456732a6cf18307244549dabc3384559c6861beb4d3be3dbb2ec64b71d3be19", expand=False, url="https://files.pythonhosted.org/packages/c1/ca/10e337628717f218cd81d4978284023a49507206b884407939c9ac8259be/hydride-0.1.0-py3-none-any.whl")
	version("1.0.0", sha256="90132f27f26bf4e9ed8871be84b96a4eb65e903212e529821cae9f6415a3982b", expand=False, url="https://files.pythonhosted.org/packages/37/af/35a3c5099559d3d84497bd52e0a45e8679b0bf7e25ebe8cc5cbfc2d8c312/hydride-1.0.0-cp39-cp39-manylinux1_x86_64.whl")
	version("1.1.0", sha256="c7f0827a919e818dccfd2e239d0188f418ee05ce4ff4d4a6e2273e237356ded2", expand=False, url="https://files.pythonhosted.org/packages/fe/00/74759e1c2099cb462fb1cfc2b5a4b5131bee9fc172e097e80b6fcae489e8/hydride-1.1.0-cp310-cp310-manylinux1_x86_64.whl")
	version("1.1.1", sha256="9dde3b7b05a4a18ace2651c66e95efa770189eda96015abb6ffb1bd872d61cb4", expand=False, url="https://files.pythonhosted.org/packages/08/08/877ad64acaf60950a41280b5d819d41b063a705042bff71dde4be6e5f82e/hydride-1.1.1-cp310-cp310-manylinux1_x86_64.whl")
	version("1.1.2", sha256="33ea8019d129bd6b7b03d01d9db5836cabfdbc1b0daabbda55a5dcb0ea69fb3c")
	version("1.2.0", sha256="60a5ba08a95a3da7e6d52787a50bb3dcaec99a473d731f20c02bb96b2d75bbf1")
	version("1.2.1", sha256="3e550f334f726c8265b2ed8b3cade500a0ac6a8476b7a1dc7f9e3965ea57d313")
	version("1.2.2", sha256="d6ba010ffe8aa80aec505ce879372749ae24fe8f402169ca18091b2cc0ec6794")
	version("1.2.3", sha256="d1d06dcfb4c4957f109bd2445a115021cf69ff7c1639cb3f96961c58b38c6453")

	depends_on("python@3.10:", type=("build", "run"))
	depends_on("py-biotite", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-cython", type=("build"))
