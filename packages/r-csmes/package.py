# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsmes(RPackage):
	"""Cost-Sensitive Multi-Criteria Ensemble Selection for Uncertain
Cost Conditions

	Functions for cost-sensitive multi-criteria ensemble selection (CSMES) (as described in De bock et al. (2020) <doi:10.1016/j.ejor.2020.01.052>) for cost-sensitive learning under unknown cost conditions.
	"""
	
	cran = "CSMES" 

	version("1.0.1", md5="af120311855dca519035f35f213da0af")

	depends_on("r-mco@1.0.15.1:", type=("build", "run"))
	depends_on("r-rocr@1.0.7:", type=("build", "run"))
	depends_on("r-rpart@4.1.15:", type=("build", "run"))
	depends_on("r-zoo@1.8.6:", type=("build", "run"))
	depends_on("r-catools@1.18:", type=("build", "run"))
	depends_on("r-data-table@1.12.2:", type=("build", "run"))
