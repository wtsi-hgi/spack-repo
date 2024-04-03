# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQch(RPackage):
	"""Query Composite Hypotheses

	Provides functions for the joint analysis of Q sets of
    p-values obtained for the same list of items. This joint analysis is
    performed by querying a composite hypothesis, i.e. an arbitrary
    complex combination of simple hypotheses, as described in Mary-Huard
    et al. (2021) <doi:10.1093/bioinformatics/btab592> and De Walsche et
    al.(2023) <doi:10.1101/2024.03.17.585412>. In this approach, the
    Q-uplet of p-values associated with each item is distributed as a
    multivariate mixture, where each of the 2^Q components corresponds to
    a specific combination of simple hypotheses. The dependence between
    the p-value series is considered using a Gaussian copula function. A
    p-value for the composite hypothesis test is derived from the
    posterior probabilities.
	"""
	
	cran = "qch" 

	version("2.0.0", md5="ba0a9551cd98ac68cc0b89b35a9bb31c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
