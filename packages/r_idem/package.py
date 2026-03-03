# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdem(RPackage):
	"""Inference in Randomized Controlled Trials with Death and
Missingness

	In randomized studies involving severely ill patients, functional
    outcomes are often unobserved due to missed clinic visits, premature
    withdrawal or death. It is well known that if these unobserved functional
    outcomes are not handled properly, biased treatment comparisons can be
    produced. In this package, we implement a procedure for comparing treatments
    that is based on the composite endpoint of both the functional outcome and
    survival. The procedure was proposed in Wang et al. (2016) <DOI:10.1111/biom.12594>
    and Wang et al. (2020) <DOI:10.18637/jss.v093.i12>. It considers missing data
    imputation with different sensitivity
    analysis strategies to handle the unobserved functional outcomes not due to
    death.
	"""
	
	homepage = "https://github.com/olssol/idem/"
	cran = "idem" 

	version("5.2", md5="ac7aad8441126a48b248d943ea55d7a0")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-sqldf@0.4:", type=("build", "run"))
	depends_on("r-survival@2.38:", type=("build", "run"))
	depends_on("r-mice@3.9:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
