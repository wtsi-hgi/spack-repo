# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHrcomprisk(RPackage):
	"""Nonparametric Assessment Between Competing Risks Hazard Ratios

	Nonparametric cumulative-incidence based estimation of the ratios of sub-hazard ratios to cause-specific hazard ratios using the approach from Ng et al. (2020).
	"""
	
	homepage = "https://github.com/AntiportaD/hrcomprisk"
	cran = "hrcomprisk" 

	version("0.1.1", md5="3fdf444d5356ae5c101b7f6c74fcd814")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
