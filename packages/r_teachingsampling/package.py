# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTeachingsampling(RPackage):
	"""Selection of Samples and Parameter Estimation in Finite
Population

	Allows the user to draw probabilistic samples and make inferences from a finite population based on several sampling designs.
	"""
	
	cran = "TeachingSampling" 

	version("4.1.1", md5="885c51e99705f7259c597290a36ece26")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
