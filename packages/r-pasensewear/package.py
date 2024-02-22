# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPasensewear(RPackage):
	"""Summarize Daily Physical Activity from 'SenseWear' Accelerometer
Data

	Provide summary table of daily physical activity and per-person/grouped heat map for accelerometer data from SenseWear Armband. See <https://templehealthcare.wordpress.com/the-sensewear-armband/> for more information about SenseWear Armband.
	"""
	
	cran = "PASenseWear" 

	version("1.0", md5="a2663a810a7e6d4eeac9460e0d8fe026")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
