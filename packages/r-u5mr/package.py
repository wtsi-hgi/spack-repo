# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RU5mr(RPackage):
	"""Under-Five Child Mortality Estimation

	Contains functions for calculating under-five child mortality estimates using the Trussell version of the Brass method (United Nations (1990) <https://www.un.org/en/development/desa/population/publications/pdf/mortality/stepguide_childmort.pdf> and United Nations (1983) <https://www.un.org/en/development/desa/population/publications/pdf/mortality/stepguide_childmort.pdf>) as well as applying the cohort-derived methods by Rajaratnam and colleagues (Rajaratnam JK, Tran LN, Lopez AD, Murray CJL (2010) "Measuring Under-Five Mortality: Validation of New Low-Cost Methods" <doi:10.1371/journal.pmed.1000253>).
	"""
	
	homepage = "https://github.com/myominnoo/u5mr"
	cran = "u5mr" 

	version("0.1.1", md5="8b18afecd665e4a7237f4755e186b9b2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
