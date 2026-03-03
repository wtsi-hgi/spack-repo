# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbck(RPackage):
	"""Statistical Bias Correction Kit

	Implementation of several recent multivariate bias correction
			 methods with a unified interface to facilitate their use. A
			 description and comparison between methods can be found
			 in <doi:10.5194/esd-11-537-2020>.
	"""
	
	homepage = "https://github.com/yrobink/SBCK"
	cran = "SBCK" 

	version("1.0.0", md5="25f6913731b5bbf7978ca8b3a459699d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-roopsd@0.3.5:", type=("build", "run"))
	depends_on("r-transport", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
