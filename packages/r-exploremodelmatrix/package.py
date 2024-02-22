# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExploremodelmatrix(RPackage):
	"""Graphical Exploration of Design Matrices

	Given a sample data table and a design formula, ExploreModelMatrix generates an interactive application for exploration of the resulting design matrix. This can be helpful for interpreting model coefficients and constructing appropriate contrasts in (generalized) linear models. Static visualizations can also be generated.
	"""
	
	homepage = "https://github.com/csoneson/ExploreModelMatrix"
	bioc = "ExploreModelMatrix" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ExploreModelMatrix_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ExploreModelMatrix/ExploreModelMatrix_1.14.0.tar.gz"]

	version("1.14.0", md5="86f96045b0ae6877428f28466b113097")

	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
