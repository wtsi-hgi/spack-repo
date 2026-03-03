# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJointpm(RPackage):
	"""Risk Estimation Using the Joint Probability Method

	Estimate risk caused by two extreme and dependent forcing variables using bivariate extreme value models as described in Zheng, Westra, and Sisson (2013) <doi:10.1016/j.jhydrol.2013.09.054>; Zheng, Westra and Leonard (2014) <doi:10.1002/2013WR014616>; Zheng, Leonard and Westra (2015) <doi:10.2166/hydro.2015.052>.
	"""
	
	cran = "jointPm" 

	version("2.3.2", md5="df1b9afb7150fa2f5dd1cd73c32afee8")

	depends_on("r@3.0.1:", type=("build", "run"))
