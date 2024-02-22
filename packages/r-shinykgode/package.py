# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinykgode(RPackage):
	"""An Interactive Application for ODE Parameter Inference Using
Gradient Matching

	An interactive Shiny application to perform fast parameter inference on
    dynamical systems (described by ordinary differential equations) using gradient matching.
    Please see the project page for more details.
	"""
	
	homepage = "https://github.com/joewandy/shinyKGode"
	cran = "shinyKGode" 

	version("1.0.5", md5="7172780d361f384e9f42c1bc6867dec5")

	depends_on("r-pracma@2.0.7:", type=("build", "run"))
	depends_on("r-pspline@1.0.18:", type=("build", "run"))
	depends_on("r-shiny@1.0.5:", type=("build", "run"))
	depends_on("r-shinyjs@0.9.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.2:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.6:", type=("build", "run"))
	depends_on("r-kgode@1:", type=("build", "run"))
	depends_on("r-xml@3.98.1.9:", type=("build", "run"))
