# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScottknottesd(RPackage):
	"""The Scott-Knott Effect Size Difference (ESD) Test

	The Scott-Knott Effect Size Difference (ESD) test is a mean comparison approach that leverages a hierarchical clustering to partition the set of treatment means (e.g., means of variable importance scores, means of model performance) into statistically distinct groups with non-negligible difference [Tantithamthavorn et al., (2018) <doi:10.1109/TSE.2018.2794977>].
	"""
	
	homepage = "https://github.com/klainfo/ScottKnottESD"
	cran = "ScottKnottESD" 

	version("2.0.3", md5="6a385a0b81938fa8e93352404d345fb9")

	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-effsize", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
