# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraper(RPackage):
	"""Adaptive penalization in high-dimensional regression and classification with external covariates using variational Bayes

	This package enables regression and classification on high-dimensional data with different relative strengths of penalization for different feature groups, such as different assays or omic types. The optimal relative strengths are chosen adaptively. Optimisation is performed using a variational Bayes approach.
	"""
	
	bioc = "graper" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/graper_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/graper/graper_1.18.0.tar.gz"]

	version("1.24.2", tag="RELEASE_3_21")
	version("1.18.0", sha256="eb08791f3163d93ecfd2a3663c6324b5f0f140849afd4a258469c7535d2b193e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
