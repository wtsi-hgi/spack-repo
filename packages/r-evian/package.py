# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvian(RPackage):
	"""Evidential Analysis of Genetic Association Data

	Evidential regression analysis for dichotomous and quantitative outcome data. The following references described the methods in this package:
        Strug, L. J., Hodge, S. E., Chiang, T., Pal, D. K., Corey, P. N., & Rohde, C. (2010) <doi:10.1038/ejhg.2010.47>.
        Strug, L. J., & Hodge, S. E. (2006) <doi:10.1159/000094709>.
        Royall, R. (1997) <ISBN:0-412-04411-0>.
	"""
	
	cran = "evian" 

	version("2.1.0", md5="c76d2fb974c7a7be7d3857a2992f23bb")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-profilelikelihood", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
