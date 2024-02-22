# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsir(RPackage):
	"""Extended State-Space SIR Models

	An implementation of extended state-space SIR models developed by
    Song Lab at UM school of Public Health. There are several functions available
    by 1) including a time-varying transmission modifier, 2) adding a time-dependent
    quarantine compartment, 3) adding a time-dependent antibody-immunization compartment.
    Wang L. (2020) <doi:10.6339/JDS.202007_18(3).0003>.
	"""
	
	cran = "eSIR" 

	version("0.4.2", md5="9aefe47a6a6df6914fe5ec0715071a2d")

	depends_on("r@3.5.2:", type=("build", "run"))
	depends_on("r-coda@0.19.3:", type=("build", "run"))
	depends_on("r-chron@2.3.54:", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-gtools@3.8.1:", type=("build", "run"))
	depends_on("r-scales@1.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-rjags@4.10:", type=("build", "run"))
