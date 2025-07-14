# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinymethyl(RPackage):
	"""Interactive visualization for Illumina methylation arrays

	Interactive tool for visualizing Illumina methylation array data. Both the 450k and EPIC array are supported.
	"""
	
	homepage = "https://github.com/Jfortin1/shinyMethyl"
	bioc = "shinyMethyl"

	version("1.44.0", commit="3ae07a15045e2b1bb7198bf070e10e0836dce324")
	version("1.38.0", commit="01d5c751c6e953ceebe7ab88b29b570722b7371a")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
