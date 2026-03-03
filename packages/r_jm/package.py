# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJm(RPackage):
	"""Joint Modeling of Longitudinal and Survival Data

	Shared parameter models for the joint modeling of longitudinal and time-to-event data. 
	"""
	
	homepage = "http://jmr.r-forge.r-project.org/"
	cran = "JM" 

	version("1.5-2", md5="19c57d95fd721c8520eee6cde08059a6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
