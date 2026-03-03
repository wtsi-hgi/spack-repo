# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbir(RPackage):
	"""Estimating the Probability of Being in Response and Related
Outcomes

	Make statistical inference on the probability of being in response, 
             the duration of response, and the cumulative response rate up to a given time point. 
             The method can be applied to analyze phase II randomized clinical trials with the endpoints 
             being time to treatment response and time to progression or death.
	"""
	
	cran = "PBIR" 

	version("0.1-0", md5="1e145dfce0a6e1a1c5922d7bc7b24cd7")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-cmprsk", type=("build", "run"))
