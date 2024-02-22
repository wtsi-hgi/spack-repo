# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoben(RPackage):
	"""Robust Bayesian Variable Selection for Gene-Environment
Interactions

	Gene-environment (G×E) interactions have important implications to elucidate the 
    etiology of complex diseases beyond the main genetic and environmental effects. 
    Outliers and data contamination in disease phenotypes of G×E studies have been commonly 
    encountered, leading to the development of a broad spectrum of robust penalization methods. 
    Nevertheless, within the Bayesian framework, the issue has not been taken care of in existing 
    studies. We develop a robust Bayesian variable selection method for G×E interaction 
    studies. The proposed Bayesian method can effectively accommodate heavy-tailed errors and 
    outliers in the response variable while conducting variable selection by accounting for 
    structural sparsity. In particular, the spike-and-slab priors have been imposed on both 
    individual and group levels to identify important main and interaction effects. An efficient 
    Gibbs sampler has been developed to facilitate fast computation. The Markov chain Monte Carlo 
    algorithms of the proposed and alternative methods are efficiently implemented in C++.
	"""
	
	homepage = "https://github.com/jrhub/roben"
	cran = "roben" 

	version("0.1.0", md5="b254b04cec501e3c7554fa6bfd3ec96d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
