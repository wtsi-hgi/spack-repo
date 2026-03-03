# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRxode2ll(RPackage):
	"""Log-Likelihood Functions for 'rxode2'

	Provides the log-likelihoods with gradients from 'stan'
    (Carpenter et al (2015), <arXiv:1509.07164>) needed
    for generalized log-likelihood estimation in 'nlmixr2'
    (Fidler et al (2019) <doi:10.1002/psp4.12445>). This is
    split of to reduce computational burden of recompiling 'rxode2'
    (Wang, Hallow and James (2016) <doi:10.1002/psp4.12052>) which runs
    the 'nlmixr2' models during estimation.
	"""
	
	homepage = "https://nlmixr2.github.io/rxode2ll/"
	cran = "rxode2ll" 

	version("2.0.11", md5="8fdf655d16c928130765788801dc8a97")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp@1.0.8:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.9.2:", type=("build", "run"))
	depends_on("r-stanheaders@2.21.0.7:", type=("build", "run"))
	depends_on("r-bh@1.78:", type=("build", "run"))
