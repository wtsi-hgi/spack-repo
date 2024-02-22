# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBspbss(RPackage):
	"""Bayesian Spatial Blind Source Separation

	Gibbs sampling for Bayesian spatial blind source separation (BSP-BSS). BSP-BSS is designed for spatially dependent signals in high dimensional and large-scale data, such as neuroimaging. The method assumes the expectation of the observed images as a linear mixture of multiple sparse and piece-wise smooth latent source signals, and constructs a Bayesian nonparametric prior by thresholding Gaussian processes. Details can be found in our paper: Wu et al. (2022+) "Bayesian Spatial Blind Source Separation via the Thresholded Gaussian Process" <doi:10.1080/01621459.2022.2123336>.
	"""
	
	cran = "BSPBSS" 

	version("1.0.5", md5="75cad5fc96ab1d0527031674d7d9afd3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-movmf", type=("build", "run"))
	depends_on("r-rstiefel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ica", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-bayesgpfit", type=("build", "run"))
	depends_on("r-svd", type=("build", "run"))
	depends_on("r-neurobase", type=("build", "run"))
	depends_on("r-oro-nifti", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
