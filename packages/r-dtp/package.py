# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtp(RPackage):
	"""Dynamic Panel Threshold Model

	Compute the dynamic threshold panel model suggested by (Stephanie Kremer, Alexander Bick and Dieter Nautz (2013) <doi:10.1007/s00181-012-0553-9>) in which they extended the (Hansen (1999) <doi: 10.1016/S0304-4076(99)00025-1>) original static panel threshold estimation and the Caner and (Hansen (2004) <doi:10.1017/S0266466604205011>) cross-sectional instrumental variable threshold model, where generalized methods of moments type estimators are used.
	"""
	
	cran = "dtp" 

	version("0.1.0", md5="51d0ec1e68c8cd3dc3019fe1c94f1378")

	depends_on("r-formula", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
