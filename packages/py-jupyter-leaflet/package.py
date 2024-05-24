# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyJupyterLeaflet(PythonPackage):
	"""ipyleaflet extensions for JupyterLab and Jupyter Notebook"""
	
	homepage = "https://github.com/jupyter-widgets/ipyleaflet"
	pypi = "jupyter-leaflet/jupyter_leaflet-0.19.1-py3-none-any.whl" 

	version("0.19.0", sha256="8bb0d7986f3cf2ce05f4036df397caa637441876fccbaaeff2c0ba5a4dfa5939", expand=False, url="https://files.pythonhosted.org/packages/b7/cc/4c964a6032a47c452cb787a9c8db037f7cc3a72364deb9ae5990eaa16297/jupyter_leaflet-0.19.0-py3-none-any.whl")
	version("0.19.1", sha256="8001a7304e9262394b8f896003539438467bed712bb9330dd65785bd9a5f8add", expand=False, url="https://files.pythonhosted.org/packages/6b/51/69ae61c456ecb27cda9e1676ee5798d10cd741579cfd292d7719d217852d/jupyter_leaflet-0.19.1-py3-none-any.whl")

	depends_on("python@3.8:", type=("build", "run"))
