# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROverlap(RPackage):
	"""Estimates of Coefficient of Overlapping for Animal Activity
Patterns

	Provides functions to fit kernel density functions to
    data on temporal activity patterns of animals; estimate coefficients
    of overlapping of densities for two species; and calculate bootstrap
    estimates of confidence intervals. As in Ridout and Linkie (2009) <doi:10.1198/jabes.2009.08038>.
	"""
	
	cran = "overlap" 

	version("0.3.9", md5="e339c76b705ce81925fcf590fae25a2a")

	depends_on("r-suntools", type=("build", "run"))
