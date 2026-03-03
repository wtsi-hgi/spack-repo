# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGp(RPackage):
	"""Maximum Likelihood Estimation of the Generalized Poisson
Distribution

	Functions to estimate the parameters of the generalized Poisson distribution with or without covariates using maximum likelihood. The references include Nikoloulopoulos A.K. & Karlis D. (2008). "On modeling count data: a comparison of some well-known discrete distributions". Journal of Statistical Computation and Simulation, 78(3): 437--457, <doi:10.1080/10629360601010760> and Consul P.C. & Famoye F. (1992). "Generalized Poisson regression model". Communications in Statistics - Theory and Methods, 21(1): 89--109, <doi:10.1080/03610929208830766>.
	"""
	
	cran = "gp" 

	version("1.1", md5="d74b360ccc59b30dc718758d5eecf9a0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rngforgpd", type=("build", "run"))
