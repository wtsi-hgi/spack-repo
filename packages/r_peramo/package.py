# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeramo(RPackage):
	"""Permutation Tests for Randomization Model

	Perform permutation-based hypothesis testing for randomized
    experiments as suggested in Ludbrook & Dudley (1998) <doi:10.2307/2685470>
    and Ernst (2004) <doi:10.1214/088342304000000396>, introduced in Pham et al.
    (2022) <doi:10.1016/j.chemosphere.2022.136736>.
	"""
	
	cran = "peramo" 

	version("0.1.3", md5="1cfcb11fb1849e3b842007355b6f8769")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-lme4@1.1.33:", type=("build", "run"))
	depends_on("r-parameters@0.21:", type=("build", "run"))
	depends_on("r-emmeans@1.8.6:", type=("build", "run"))
