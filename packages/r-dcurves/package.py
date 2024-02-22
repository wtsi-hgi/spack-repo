# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcurves(RPackage):
	"""Decision Curve Analysis for Model Evaluation

	Diagnostic and prognostic models are typically evaluated with
    measures of accuracy that do not address clinical consequences.
    Decision-analytic techniques allow assessment of clinical outcomes,
    but often require collection of additional information may be
    cumbersome to apply to models that yield a continuous result. Decision
    curve analysis is a method for evaluating and comparing prediction
    models that incorporates clinical consequences, requires only the data
    set on which the models are tested, and can be applied to models that
    have either continuous or dichotomous results. See the following references 
    for details on the methods: Vickers (2006) <doi:10.1177/0272989X06295361>,
    Vickers (2008) <doi:10.1186/1472-6947-8-53>, 
    and Pfeiffer (2020) <doi:10.1002/bimj.201800240>.
	"""
	
	homepage = "https://github.com/ddsjoberg/dcurves"
	cran = "dcurves" 

	version("0.4.0", md5="6d5619063a1197bbde84b0a21c7d5eb1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-broom@0.7.10:", type=("build", "run"))
	depends_on("r-dplyr@1.0.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tibble@3.1:", type=("build", "run"))
