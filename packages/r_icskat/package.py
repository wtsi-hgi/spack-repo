# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcskat(RPackage):
	"""Interval-Censored Sequence Kernel Association Test

	Implements the Interval-Censored Sequence Kernel Association (ICSKAT) test for testing the association between interval-censored time-to-event outcomes and groups of single nucleotide polymorphisms (SNPs). Interval-censored time-to-event data occur when the event time is not known exactly but can be deduced to fall within a given interval. For example, some medical conditions like bone mineral density deficiency are generally only diagnosed at clinical visits. If a patient goes for clinical checkups yearly and is diagnosed at, say, age 30, then the onset of the deficiency is only known to fall between the date of their age 29 checkup and the date of the age 30 checkup. Interval-censored data include right- and left-censored data as special cases. This package also implements the interval-censored Burden test and the ICSKATO test, which is the optimal combination of the ICSKAT and Burden tests. Please see the vignette for a quickstart guide.
	"""
	
	cran = "ICSKAT" 

	version("0.2.0", md5="e9573016f21ff7ccad290bbeb21a9afa")

	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rje", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
