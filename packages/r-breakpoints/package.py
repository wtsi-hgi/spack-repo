# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreakpoints(RPackage):
	"""Identify Breakpoints in Series of Data

	Compute Buishand Range Test, Pettit Test, SNHT, Student t-test, and Mann-Whitney Rank Test, to identify breakpoints in series. For all functions NA is allowed. Since all of the mention methods identify only one breakpoint in a series, a general function to look for N breakpoint is given. Also, the Yamamoto test for climate jump is available. Alexandersson, H. (1986) <doi:10.1002/joc.3370060607>, Buishand, T. (1982) <doi:10.1016/0022-1694(82)90066-X>, Hurtado, S. I., Zaninelli, P. G., & Agosta, E. A. (2020) <doi:10.1016/j.atmosres.2020.104955>, Mann, H. B., Whitney, D. R. (1947) <doi:10.1214/aoms/1177730491>, Pettitt, A. N. (1979) <doi:10.2307/2346729>, Ruxton, G. D., jul (2006) <doi:10.1093/beheco/ark016>, Yamamoto, R., Iwashima, T., Kazadi, S. N., & Hoshiai, M. (1985) <doi:10.2151/jmsj1965.63.6_1157>.
	"""
	
	cran = "BreakPoints" 

	version("1.2", md5="7b1a5f874e5cc32cf331496bdb64a43c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
