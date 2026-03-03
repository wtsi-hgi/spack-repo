# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpmlecmprsk(RPackage):
	"""Type-Specific Failure Rate and Hazard Rate on Competing Risks
Data

	Given a failure type, the function computes covariate-specific probability of failure over time and covariate-specific conditional hazard rate based on possibly right-censored competing risk data. Specifically, it computes the non-parametric maximum-likelihood estimates of these quantities and their asymptotic variances in a semi-parametric mixture model for competing-risks data, as described in Chang et al. (2007a).
	"""
	
	cran = "NPMLEcmprsk" 

	version("3.0", md5="57c58921d9f1e8e9c0545135b71be4c3")

