# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTactile(RPackage):
	"""New and Extended Plots, Methods, and Panel Functions for
'lattice'

	Extensions to 'lattice', providing new high-level
    functions, methods for existing functions, panel functions, and a theme.
	"""
	
	homepage = "https://github.com/jolars/tactile"
	cran = "tactile" 

	version("0.2.1", md5="212367f76ee81c563ebc5f0aa12d397f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
