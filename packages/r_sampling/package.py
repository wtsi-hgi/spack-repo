# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSampling(RPackage):
	"""Survey Sampling

	Functions to draw random samples using different sampling schemes are available. Functions are also provided to obtain (generalized) calibration weights, different estimators, as well some variance estimators.  
	"""
	
	cran = "sampling" 

	version("2.10", md5="42f9a999adb8edaa1aa1199d1774b8aa")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
