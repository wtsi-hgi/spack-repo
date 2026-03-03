# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhotobiologylamps(RPackage):
	"""Spectral Irradiance Data for Lamps

	Spectral emission data for some frequently used lamps including 
    bulbs and flashlights based on led emitting diodes (LEDs) but excluding
    LEDs available as electronic components. Original spectral irradiance data 
    for incandescent-, LED- and discharge lamps are included. They are 
    complemented by data on the effect of temperature on the emission by 
    fluorescent tubes. Part of the 'r4photobiology' suite, Aphalo P. J. (2015) 
    <doi:10.19232/uv4pb.2015.1.14>.
	"""
	
	homepage = "https://www.r4photobiology.info/"
	cran = "photobiologyLamps" 

	version("0.5.2", md5="620bdc00a0e64d7ee1745ccb4f320602")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-photobiology@0.11:", type=("build", "run"))
