# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSleepcycles(RPackage):
	"""Sleep Cycle Detection

	Sleep cycles are largely detected according to the originally proposed criteria by Feinberg & Floyd (1979) <doi:10.1111/j.1469-8986.1979.tb02991.x> as described in Blume & Cajochen (2021) <doi:10.1016/j.mex.2021.101318>. 
	"""
	
	cran = "SleepCycles" 

	version("1.1.4", md5="ae5cdf565db4b0d0a49f2e83b3846df9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
