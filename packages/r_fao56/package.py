# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFao56(RPackage):
	"""Evapotranspiration Based on FAO Penman-Monteith Equation

	Calculation of Evapotranspiration by FAO Penman-Monteith equation based on Allen, R. G., Pereira, L. S., Raes, D., Smith, M. (1998, ISBN:92-5-104219-5) "Crop evapotranspiration - Guidelines for computing crop water requirements - FAO Irrigation and drainage paper 56".
	"""
	
	cran = "FAO56" 

	version("1.0", md5="321c8f4d00dea8ff78712ecbd060d70b", url="https://cran.r-project.org/src/contrib/FAO56_1.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
