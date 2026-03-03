# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeepgp(RPackage):
	"""Bayesian Deep Gaussian Processes using MCMC

	Performs Bayesian posterior inference for deep Gaussian processes following 
    Sauer, Gramacy, and Higdon (2023, <arXiv:2012.08015>).  See Sauer (2023,
    <http://hdl.handle.net/10919/114845>) for comprehensive methodological details and
    <https://bitbucket.org/gramacylab/deepgp-ex/> for a variety of coding examples. 
    Models are trained through
    MCMC including elliptical slice sampling of latent Gaussian layers and Metropolis-Hastings
    sampling of kernel hyperparameters.  Vecchia-approximation for faster computation is implemented
    following Sauer, Cooper, and Gramacy (2022, <arXiv:2204.02904>).  Downstream tasks include
    sequential design through active learning Cohn/integrated mean squared error (ALC/IMSE; Sauer, 
    Gramacy, and Higdon, 2023), optimization through expected improvement (EI; 
    Gramacy, Sauer, and Wycoff, 2021 <arXiv:2112.07457>), and contour location through entropy
    (Sauer, 2023).  Models extend up to three layers deep; a one layer model is equivalent to 
    typical Gaussian process regression.  Incorporates OpenMP and SNOW parallelization and 
    utilizes C/C++ under the hood.
	"""
	
	cran = "deepgp" 

	version("1.1.1", md5="743a848301e08950531447921093fe17")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-gpgp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
