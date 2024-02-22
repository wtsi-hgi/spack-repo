# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcci(RPackage):
	"""Feldman-Cousins Confidence Intervals

	
	Provides support for building Feldman-Cousins confidence intervals 
	[G. J. Feldman and R. D. Cousins (1998) <doi:10.1103/PhysRevD.57.3873>].
	"""
	
	homepage = "https://github.com/vgherard/fcci"
	cran = "fcci" 

	version("1.0.1", md5="bb753a905ba831f66463a954509cff40")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
