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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/gespeR_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/gespeR/gespeR_1.34.0.tar.gz"]

	version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="4ab88430573c331e671c94059749d8c5689423ee1bffcb95aa4428e843b2f1b2")

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
