# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmgampoi(RPackage):
	"""Fit a Gamma-Poisson Generalized Linear Model.

	Fit linear models to overdispersed count data.  The package can estimate
	the overdispersion and fit repeated models for matrix input. It is designed
	to handle large input datasets as they typically occur in single cell
	RNA-seq experiments."""

	bioc = "glmGamPoi"
	version("1.20.0", commit="6fb5b42e9869bc8a92f720a4a24e2f6afab37711")
	version("1.8.0", commit="b723d61e05c1ad50a3cf6a6393ec3d97adc7edb4")
	version("1.6.0", commit="03df1e116df7ed6997401470bfc52619874641a1")
	version("1.14.3", md5="a713a5c0adddd2e5f4d30e02af38d309")
	version("1.12.0", commit="5fdfa5ca1a56b19e51bc6e307ca6015cc56109a0")
	version("1.10.0", commit="048e17384209fc07031e09875ec6eea35e90ef46")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-beachmat", type=("build", "run"))
