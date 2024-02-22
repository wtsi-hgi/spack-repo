# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTableeasy(RPackage):
	"""Tables of Clinical Study

	Creates some tables of clinical study. 'Table 1' is created by table1() to describe baseline characteristics, which is essential in every clinical study. Created by table2(), the function of 'Table 2' is to explore influence factors. And 'Table 3' created by table3() is able to make stratified analysis.
	"""
	
	cran = "tableeasy" 

	version("1.1.2", md5="b944b5addb6a1ae22e1ad8905f846618")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-tableone", type=("build", "run"))
