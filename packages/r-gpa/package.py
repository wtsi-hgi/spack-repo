# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpa(RPackage):
	"""GPA (Genetic analysis incorporating Pleiotropy and Annotation)

	This package provides functions for fitting GPA, a statistical framework to prioritize GWAS results by integrating pleiotropy information and annotation data. In addition, it also includes ShinyGPA, an interactive visualization toolkit to investigate pleiotropic architecture.
	"""
	
	homepage = "http://dongjunchung.github.io/GPA/"
	bioc = "GPA"

	version("1.20.0", commit="7d9e78d417f7ef08106223b54f8f9cc3ce23654c")
	version("1.14.0", commit="5a54bed394d82ea9afda314a3b7085f3b9e00d0a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
