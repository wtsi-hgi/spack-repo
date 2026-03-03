# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastbeta(RPackage):
	"""Fast Estimation of Time-Varying Infectious Disease Transmission
Rates

	Methods for estimating time-varying infectious disease
	transmission rates from disease incidence time series, based
	on discretizations of an SIR model, as analyzed in Jagan et al.
	(2020) <doi:10.1371/journal.pcbi.1008124>.
	"""
	
	homepage = "https://github.com/davidearn/fastbeta"
	cran = "fastbeta" 

	version("0.2.0", md5="be4432b2daccf314cb133ed738a132f7")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-adaptivetau", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
