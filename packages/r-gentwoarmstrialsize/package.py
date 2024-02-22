# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGentwoarmstrialsize(RPackage):
	"""Generalized Two Arms Clinical Trial Sample Size Calculation

	Two arms clinical trials required sample size is calculated in the comprehensive parametric context. The calculation is based on the type of endpoints(continuous/binary/time-to-event/ordinal), design (parallel/crossover), hypothesis tests (equality/noninferiority/superiority/equivalence), trial arms noncompliance rates and expected loss of follow-up. Methods are described in: Chow SC, Shao J, Wang H, Lokhnygina Y (2017) <doi:10.1201/9781315183084>, Wittes, J (2002) <doi:10.1093/epirev/24.1.39>, Sato, T (2000) <doi:10.1002/1097-0258(20001015)19:19%3C2689::aid-sim555%3E3.0.co;2-0>, Lachin J M, Foulkes, M A (1986) <doi:10.2307/2531201>, Whitehead J(1993) <doi:10.1002/sim.4780122404>, Julious SA (2023) <doi:10.1201/9780429503658>.
	"""
	
	cran = "GenTwoArmsTrialSize" 

	version("0.0.4.5", md5="36b5fc3b2116bf33efdf9f588147c050")

	depends_on("r-trialsize", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
