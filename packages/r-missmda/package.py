# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMissmda(RPackage):
	"""Handling Missing Values with Multivariate Data Analysis

	Imputation of incomplete continuous or categorical datasets; Missing values are imputed with a principal component analysis (PCA), a multiple correspondence analysis (MCA) model or a multiple factor analysis (MFA) model; Perform multiple imputation with and in PCA or MCA.
	"""
	
	homepage = "http://factominer.free.fr/missMDA/index.html"
	cran = "missMDA" 

	version("1.19", md5="1c20cd23a2531d67d6ea3400cec4ece4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-factominer@2.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
