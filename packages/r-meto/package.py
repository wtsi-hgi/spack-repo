# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeto(RPackage):
	"""Meteorological Tools

	Meteorological Tools following the FAO56 irrigation paper of Allen et al. (1998) [1].
    Functions for calculating:
    reference evapotranspiration (ETref),
    extraterrestrial radiation (Ra),
    net radiation (Rn),
    saturation vapor pressure (satVP),
    global radiation (Rs),
    soil heat flux (G),
    daylight hours,
    and more.
    [1] Allen, R. G., Pereira, L. S., Raes, D., & Smith, M. (1998). Crop evapotranspiration-Guidelines for computing crop water requirements-FAO Irrigation and drainage paper 56. FAO, Rome, 300(9).
	"""
	
	cran = "MeTo" 

	version("0.1.1", md5="05d15e8723bc632491ec106c9f489cdb")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
