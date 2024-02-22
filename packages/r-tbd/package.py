# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTbd(RPackage):
	"""Estimation of Causal Effects with Outcomes Truncated by Death

	Estimation of the survivor average causal effect under outcomes truncated by death, which requires the existence of a substitution variable. It can be applied to both experimental and observational data.
	"""
	
	homepage = "https://github.com/KillingVectorField/causal-inference-truncated-by-death"
	cran = "tbd" 

	version("0.1.0", md5="7150c5a20914dede6f623f03ddc31799")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
