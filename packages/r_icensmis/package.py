# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcensmis(RPackage):
	"""Study Design and Data Analysis in the Presence of Error-Prone
Diagnostic Tests and Self-Reported Outcomes

	We consider studies in which information from error-prone
    diagnostic tests or self-reports are gathered sequentially to determine the
    occurrence of a silent event. Using a likelihood-based approach
    incorporating the proportional hazards assumption, we provide functions to
    estimate the survival distribution and covariate effects. We also provide 
    functions for power and sample size calculations for this setting.
    Please refer to Xiangdong Gu, Yunsheng Ma, and Raji Balasubramanian (2015) 
    <doi: 10.1214/15-AOAS810>, Xiangdong Gu and Raji Balasubramanian (2016) 
    <doi: 10.1002/sim.6962>, Xiangdong Gu, Mahlet G Tadesse, Andrea S Foulkes,
    Yunsheng Ma, and Raji Balasubramanian (2020) <doi: 10.1186/s12911-020-01223-w>.
	"""
	
	cran = "icensmis" 

	version("1.5.0", md5="8c69238e20206cb1e31c5052a7f683b7")

	depends_on("r-rcpp", type=("build", "run"))
