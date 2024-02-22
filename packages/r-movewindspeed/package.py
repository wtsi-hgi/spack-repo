# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMovewindspeed(RPackage):
	"""Estimate Wind Speeds from Bird Trajectories

	Estimating wind speed from trajectories of individually tracked birds using a maximum likelihood approach.
	"""
	
	homepage = "https://gitlab.com/bartk/moveWindSpeed"
	cran = "moveWindSpeed" 

	version("0.2.4", md5="8766c91a0cf56b222d1c814ae1d4d0c1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-move", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
