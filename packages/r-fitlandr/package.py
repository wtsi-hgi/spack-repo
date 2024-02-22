# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitlandr(RPackage):
	"""Fit Vector Fields and Potential Landscapes from Intensive
Longitudinal Data

	A toolbox for estimating vector fields from intensive
    longitudinal data, and construct potential landscapes thereafter. The
    vector fields can be estimated with two nonparametric methods: the
    Multivariate Vector Field Kernel Estimator (MVKE) by Bandi & Moloche
    (2018) <doi:10.1017/S0266466617000305> and the Sparse Vector Field
    Consensus (SparseVFC) algorithm by Ma et al.  (2013)
    <doi:10.1016/j.patcog.2013.05.017>. The potential landscapes can be
    constructed with a simulation-based approach with the 'simlandr'
    package (Cui et al., 2021) <doi:10.31234/osf.io/pzva3>, or the
    Bhattacharya et al. (2011) method for path integration
    <doi:10.1186/1752-0509-5-85>.
	"""
	
	homepage = "https://sciurus365.github.io/fitlandr/"
	cran = "fitlandr" 

	version("0.1.0", md5="e923ccf2e78f990e390ad5982c6e492d")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-simlandr@0.3:", type=("build", "run"))
	depends_on("r-sparsevfc", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
