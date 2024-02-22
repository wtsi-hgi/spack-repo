# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaxpro(RPackage):
	"""Maximum Projection Designs

	Generate maximum projection (MaxPro) designs for quantitative and/or qualitative factors. Details of the MaxPro criterion can be found in: (1) Joseph, Gul, and Ba. (2015) "Maximum Projection Designs for Computer Experiments", Biometrika, 102, 371-380, and (2) Joseph, Gul, and Ba. (2018) "Designing Computer Experiments with Multiple Types of Factors: The MaxPro Approach", Journal of Quality Technology, to appear.
	"""
	
	cran = "MaxPro" 

	version("4.1-2", md5="06aadce439e3ba456c554336c4f6bf96")

	depends_on("r-nloptr", type=("build", "run"))
