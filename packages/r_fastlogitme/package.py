# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastlogitme(RPackage):
	"""Basic Marginal Effects for Logit Models

	Calculates marginal effects based on logistic model objects such as 'glm' or 'speedglm' at the average (default) or at given values using finite differences. It also returns confidence intervals for said marginal effects and the p-values, which can easily be used as input in stargazer. The function only returns the essentials and is therefore much faster but not as detailed as other functions available to calculate marginal effects. As a result, it is highly suitable for large datasets for which other packages may require too much time or calculating power.
	"""
	
	cran = "fastlogitME" 

	version("0.1.0", md5="7362f591315f94ed6ff62beedd273a7e")

