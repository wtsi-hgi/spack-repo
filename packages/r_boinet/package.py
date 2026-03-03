# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoinet(RPackage):
	"""Conduct Simulation Study of Bayesian Optimal Interval Design
with BOIN-ET Family

	Bayesian optimal interval based on both efficacy and toxicity outcomes (BOIN-ET) design is a model-assisted oncology phase I/II trial design, aiming to establish an optimal biological dose accounting for efficacy and toxicity in the framework of dose-finding. Some extensions of BOIN-ET design are also available to allow for time-to-event efficacy and toxicity outcomes based on cumulative and pending data (time-to-event BOIN-ET: TITE-BOIN-ET), ordinal graded efficacy and toxicity outcomes (generalized BOIN-ET: gBOIN-ET), and their combination (TITE-gBOIN-ET). 'boinet' is a package to implement the BOIN-ET design family and supports the conduct of simulation studies to assess operating characteristics of BOIN-ET, TITE-BOIN-ET, gBOIN-ET, and TITE-gBOIN-ET, where users can choose design parameters in flexible and straightforward ways depending on their own application.
	"""
	
	cran = "boinet" 

	version("1.0.0", md5="e638e5f40ed29dff459463d211a20f80")

	depends_on("r-iso", type=("build", "run"))
	depends_on("r-mfp", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
