# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopsiswm(RPackage):
	"""Multi-Criteria Method for Decision (TOPSIS)

	Assists in the TOPSIS analysis process, designed to return at the end of the answer of the TOPSIS multicriteria analysis,  a ranking table with the best option as the analysis proposes. TOPSIS is basically a technique developed by Hwang and Yoon in 1981, starting from the point that the best alternative should be closest to the positive ideal solution and farthest from the negative one, based on several criteria to result in the best benefit. (LIU, H. et al., 2019) <doi:10.1016/j.agwat.2019.105787>.
	"""
	
	cran = "TopSisWM" 

	version("1.0.2", md5="a73a95c9e64f2aa8293f25ef45de5ba2")

	depends_on("r@2.10:", type=("build", "run"))
