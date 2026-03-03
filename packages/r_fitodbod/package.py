# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitodbod(RPackage):
	"""Modeling Over Dispersed Binomial Outcome Data Using BMD and ABD

	Contains Probability Mass Functions, Cumulative Mass
    Functions, Negative Log Likelihood value, parameter estimation and
    modeling data using Binomial Mixture Distributions (BMD) (Manoj et al
    (2013) <doi:10.5539/ijsp.v2n2p24>) and Alternate Binomial
    Distributions (ABD) (Paul (1985) <doi:10.1080/03610928508828990>),
    also Journal article to use the package(<doi:10.21105/joss.01505>).
	"""
	
	homepage = "https://github.com/Amalan-ConStat/fitODBOD"
	cran = "fitODBOD" 

	version("1.5.1", md5="cce168be5cc5c6e82c5730876c1bf1d9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bbmle", type=("build", "run"))
	depends_on("r-hypergeo", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
