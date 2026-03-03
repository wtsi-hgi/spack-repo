# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsrsb(RPackage):
	"""Group Sequential Refined Secondary Boundary

	A gate-keeping procedure to test a primary and a secondary endpoint in a group sequential design with multiple interim looks. Computations related to group sequential primary and secondary boundaries. Refined secondary boundaries are calculated for a gate-keeping test on a primary and a secondary endpoint in a group sequential design with multiple interim looks. The choices include both the standard boundaries and the boundaries using error spending functions. 
    See Tamhane et al. (2018), "A gatekeeping procedure to test a primary and a secondary endpoint in a group sequential design with multiple interim looks", Biometrics, 74(1), 40-48. 
	"""
	
	cran = "gsrsb" 

	version("1.2.1", md5="590fa494f50d5a5536dad312670c61f1")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1:", type=("build", "run"))
	depends_on("r-ldbounds@2:", type=("build", "run"))
	depends_on("r-xtable@1.8:", type=("build", "run"))
