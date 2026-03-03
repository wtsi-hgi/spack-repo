# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarimp(RPackage):
	"""RF Variable Importance for Arbitrary Measures

	Computes the random forest variable importance (VIMP) for the conditional inference random forest (cforest) of the 'party' package. Includes a function (varImp) that computes the VIMP for arbitrary measures from the 'measures' package. For calculating the VIMP regarding the measures accuracy and AUC two extra functions exist (varImpACC and varImpAUC).
	"""
	
	cran = "varImp" 

	version("0.4", md5="f81998a7e9d526b882b4ee5c6e330d17")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-measures", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
