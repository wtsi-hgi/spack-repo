# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGesper(RPackage):
	"""Gene-Specific Phenotype EstimatoR

	Estimates gene-specific phenotypes from off-target confounded RNAi screens. The phenotype of each siRNA is modeled based on on-targeted and off-targeted genes, using a regularized linear regression model.
	"""
	
	homepage = "http://www.cbg.ethz.ch/software/gespeR"
	bioc = "gespeR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/gespeR_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/gespeR/gespeR_1.34.0.tar.gz"]

	version("1.34.0", md5="b29c5440e5f853e993e3ca2df2eae3e6")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-cellhts2", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
