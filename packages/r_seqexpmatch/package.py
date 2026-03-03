# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqexpmatch(RPackage):
	"""Sequential Experimental Design via Matching on-the-Fly

	Generates the following sequential two-arm experimental designs:
    (1) completely randomized (Bernoulli)
    (2) balanced completely randomized
    (3) Efron's (1971) Biased Coin
    (4) Atkinson's (1982) Covariate-Adjusted Biased Coin
    (5) Kapelner and Krieger's (2014) Covariate-Adjusted Matching on the Fly
    (6) Kapelner and Krieger's (2021) CARA Matching on the Fly with Differential Covariate Weights (Naive)
    (7) Kapelner and Krieger's (2021) CARA Matching on the Fly with Differential Covariate Weights (Stepwise)
    and also provides the following types of inference:
    (1) estimation (with both Z-style estimators and OLS estimators), 
    (2) frequentist testing (via asymptotic distribution results and via employing the nonparametric randomization test) and
    (3) frequentist confidence intervals (only under the superpopulation sampling assumption currently). Details can be found
    in our publication: Kapelner and Krieger "A Matching Procedure for Sequential Experiments that Iteratively Learns which 
    Covariates Improve Power" (2020) <arXiv:2010.05980>.
	"""
	
	homepage = "https://github.com/kapelner/matching_on_the_fly_designs_R_package_and_paper_repr"
	cran = "SeqExpMatch" 

	version("0.1.0", md5="f07e5176d152b594c2039ebf7b2bd74e")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r@3.6.3:", type=("build", "run"))
