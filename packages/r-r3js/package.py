# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR3js(RPackage):
	"""'WebGL'-Based 3D Plotting using the 'three.js' Library

	Provides R and 'JavaScript' functions to allow 'WebGL'-based 3D plotting
    using the 'three.js' 'JavaScript' library. Interactivity through roll-over 
    highlighting and toggle buttons is also supported.
	"""
	
	cran = "r3js" 

	version("0.0.2", md5="720b56a847223aae2c0c6767591fb934")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
