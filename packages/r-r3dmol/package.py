# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR3dmol(RPackage):
	"""Create Interactive 3D Visualizations of Molecular Data

	Create rich and fully interactive 3D visualizations of molecular data.
    Visualizations can be included in Shiny apps and R markdown documents, or viewed
    from the R console and 'RStudio' Viewer. 'r3dmol' includes an extensive API
    to manipulate the visualization after creation, and supports getting data out of
    the visualization into R. Based on the '3dmol.js' and the 'htmlwidgets' R package.
	"""
	
	homepage = "https://github.com/swsoyee/r3dmol"
	cran = "r3dmol" 

	version("0.1.2", md5="c86cae09a188332513e18ea574c4fe89")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-bio3d", type=("build", "run"))
