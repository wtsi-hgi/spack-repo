# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReflimr(RPackage):
	"""Reference Limit Estimation Using Routine Laboratory Data

	Uses an indirect method based on truncated quantile-quantile plots to estimate reference limits from routine laboratory data. The principle of the method was developed by Robert G Hoffmann (1963) <doi:10.1001/jama.1963.03060110068020> and modified by Georg Hoffmann and colleagues (2015) <doi:10.1515/labmed-2015-0104>, (2020) <doi:10.1515/labmed-2020-0005>, and (2022) <doi:10.1007/978-3-031-15509-3_31>. 
	"""
	
	homepage = "https://github.com/reflim/reflimR"
	cran = "reflimR" 

	version("1.0.6", md5="774e16d9a651a4dcbb07baca5fd86264")

	depends_on("r@3.5:", type=("build", "run"))
