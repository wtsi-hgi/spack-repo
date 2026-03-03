# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMidrangemcp(RPackage):
	"""Multiples Comparisons Procedures Based on Studentized Midrange
and Range Distributions

	Apply tests of multiple comparisons based
    on studentized 'midrange' and 'range' distributions. 
    The tests are: Tukey Midrange ('TM' test),
    Student-Newman-Keuls Midrange ('SNKM' test), 
    Means Grouping Midrange ('MGM' test) and 
    Means Grouping Range ('MGR' test). The first two tests were published by 
    Batista and Ferreira (2020) <doi:10.1590/1413-7054202044008020>. 
    The last two are being published.
	"""
	
	homepage = "https://bendeivide.github.io/midrangeMCP/"
	cran = "midrangeMCP" 

	version("3.1.1", md5="88867ba9571f1b4a4777b6c8df520b61")

	depends_on("r-smr", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
