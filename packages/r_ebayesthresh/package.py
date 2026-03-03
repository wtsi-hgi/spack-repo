# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbayesthresh(RPackage):
	"""Empirical Bayes Thresholding and Related Methods

	Empirical Bayes thresholding using the methods developed
    by I. M. Johnstone and B. W. Silverman. The basic problem is to
    estimate a mean vector given a vector of observations of the mean
    vector plus white noise, taking advantage of possible sparsity in
    the mean vector. Within a Bayesian formulation, the elements of
    the mean vector are modelled as having, independently, a
    distribution that is a mixture of an atom of probability at zero
    and a suitable heavy-tailed distribution. The mixing parameter can
    be estimated by a marginal maximum likelihood approach. This leads
    to an adaptive thresholding approach on the original data.
    Extensions of the basic method, in particular to wavelet
    thresholding, are also implemented within the package.
	"""
	
	homepage = "https://github.com/stephenslab/EbayesThresh"
	cran = "EbayesThresh" 

	version("1.4-12", md5="ef1bda302ae53aee2907dd038cb09a11")

	depends_on("r-wavethresh", type=("build", "run"))
