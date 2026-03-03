# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClinicaltrialsummary(RPackage):
	"""Summary Measures for Clinical Trials with Survival Outcomes

	Provides estimates of several summary measures for clinical trials including
    the average hazard ratio, the weighted average hazard ratio, the restricted 
    superiority probability ratio, the restricted mean survival difference and 
    the ratio of restricted mean times lost, based on the short-term and 
    long-term hazard ratio model (Yang, 2005 <doi:10.1093/biomet/92.1.1>) 
    which accommodates various non-proportional hazards scenarios. The inference
    procedures and the asymptotic results for the summary measures are discussed 
    in Yang (2018, <doi:10.1002/sim.7676>).
	"""
	
	cran = "ClinicalTrialSummary" 

	version("1.1.1", md5="f9b22f9e71c8dfbb3866cd0605c23ef7")

	depends_on("r-rcpp", type=("build", "run"))
