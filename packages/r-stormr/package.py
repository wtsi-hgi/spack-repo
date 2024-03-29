# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStormr(RPackage):
	"""Analyzing the Behaviour of Wind Generated by Tropical Storms and
Cyclones

	Set of functions to quantify and map the
    behaviour of winds generated by tropical storms and cyclones in space
    and time. It includes functions to compute and analyze fields such as the maximum sustained wind field, power dissipation index and duration of exposure to winds above a given threshold. It also includes functions to map the trajectories as well as characteristics of the storms.
	"""
	
	homepage = "https://umr-amap.github.io/StormR/"
	cran = "StormR" 

	version("0.1.1", md5="e1f583b101b594904e45be595c92882b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-rworldmap", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
