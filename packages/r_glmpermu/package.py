# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmpermu(RPackage):
	"""Permutation-Based Inference for Generalized Linear Models

	In practical applications, the assumptions underlying generalized linear models frequently face violations, including incorrect specifications of the outcome variable's distribution or omitted predictors. These deviations can render the results of standard generalized linear models unreliable. As the sample size increases, what might initially appear as minor issues can escalate to critical concerns. To address these challenges, we adopt a permutation-based inference method tailored for generalized linear models. This approach offers robust estimations that effectively counteract the mentioned problems, and its effectiveness remains consistent regardless of the sample size.
	"""
	
	cran = "glmpermu" 

	version("0.0.1", md5="3e653dd55b456aa2a74c18f1ad0dee38")

