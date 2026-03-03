# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubmax(RPackage):
	"""Effect Modification in Observational Studies Using the Submax
Method

	Effect modification occurs if a treatment effect is larger or more stable in certain subgroups defined by observed covariates.  The submax or subgroup-maximum method of Lee et al. (2017) <arXiv:1702.00525> does an overall test and separate tests in subgroups, correcting for multiple testing using the joint distribution.
	"""
	
	cran = "submax" 

	version("1.1.1", md5="3bb11df02878c16988f7ad93cffaff63")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-sensitivityfull", type=("build", "run"))
