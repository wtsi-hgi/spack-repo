# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesmallows(RPackage):
	"""Bayesian Preference Learning with the Mallows Rank Model

	An implementation of the Bayesian version of the Mallows rank model
    (Vitelli et al., Journal of Machine Learning Research, 2018 <https://jmlr.org/papers/v18/15-481.html>;
    Crispino et al., Annals of Applied Statistics, 2019 <doi:10.1214/18-AOAS1203>;
    Sorensen et al., R Journal, 2020 <doi:10.32614/RJ-2020-026>;
    Stein, PhD Thesis, 2023 <https://eprints.lancs.ac.uk/id/eprint/195759>). Both Metropolis-Hastings
    and sequential Monte Carlo algorithms for estimating the models are available. Cayley, footrule,
    Hamming, Kendall, Spearman, and Ulam distances are supported in the models. The rank data to be
    analyzed can be in the form of complete rankings, top-k rankings, partially missing rankings, as well
    as consistent and inconsistent pairwise preferences. Several functions for plotting and studying the
    posterior distributions of parameters are provided. The package also provides functions for estimating
    the partition function (normalizing constant) of the Mallows rank model, both with the importance
    sampling algorithm of Vitelli et al. and asymptotic approximation with the IPFP algorithm
    (Mukherjee, Annals of Statistics, 2016 <doi:10.1214/15-AOS1389>).
	"""
	
	homepage = "https://github.com/ocbe-uio/BayesMallows"
	cran = "BayesMallows" 

	version("2.1.0", md5="e64c0b55633ff8976c9ae43d1e7e1723")
	version("2.1.1", md5="3672a54d8381aaa60eba20229d018c7b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-rdpack@1:", type=("build", "run"))
	depends_on("r-igraph@1.2.5:", type=("build", "run"))
	depends_on("r-sets@1.0.18:", type=("build", "run"))
	depends_on("r-relations@0.6.8:", type=("build", "run"))
	depends_on("r-rlang@0.3.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
