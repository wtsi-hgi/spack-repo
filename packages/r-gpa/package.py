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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GPA_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GPA/GPA_1.14.0.tar.gz"]

	version("1.14.0", sha256="8a624b975b10839dcca12b0e191ec749ddf1e9afeb88a42bcbba21de48048c25")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
