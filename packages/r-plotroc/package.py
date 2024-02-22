# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotroc(RPackage):
	"""Generate Useful ROC Curve Charts for Print and Interactive Use

	Most ROC curve plots obscure the cutoff values and inhibit
    interpretation and comparison of multiple curves. This attempts to address
    those shortcomings by providing plotting and interactive tools. Functions
    are provided to generate an interactive ROC curve plot for web use, and
    print versions. A Shiny application implementing the functions is also
    included.
	"""
	
	homepage = "https://sachsmc.github.io/plotROC/"
	cran = "plotROC" 

	version("2.3.1", md5="35293fe529065f3c6f23aea0586a6154")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridsvg", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
