# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransformgampoi(RPackage):
	"""Variance Stabilizing Transformation for Gamma-Poisson Models

	Variance-stabilizing transformations help with the analysis of heteroskedastic data (i.e., data where the variance is not constant, like count data). This package provide two types of variance stabilizing transformations: (1) methods based on the delta method (e.g., 'acosh', 'log(x+1)'), (2) model residual based (Pearson and randomized quantile residuals).
	"""
	
	homepage = "https://github.com/const-ae/transformGamPoi"
	bioc = "transformGamPoi" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/transformGamPoi_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/transformGamPoi/transformGamPoi_1.8.0.tar.gz"]

	version("1.8.0", sha256="3d28f9317d5b826507beebb481befab6f7310f22277d0d39ec526b30b5874775")

	depends_on("r-glmgampoi", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
