# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHurreconr(RPackage):
	"""Models Hurricane Wind Speed, Wind Direction, and Wind Damage

	The HURRECON model estimates wind speed, wind direction, enhanced 
    Fujita scale wind damage, and duration of EF0 to EF5 winds as a function 
    of hurricane location and maximum sustained wind speed. Results may be 
    generated for a single site or an entire region. Hurricane track and 
    intensity data may be imported directly from the US National Hurricane 
    Center's HURDAT2 database. For details on the original version of the 
    model written in Borland Pascal, see: Boose, Chamberlin, and Foster (2001) 
    <doi:10.1890/0012-9615(2001)071[0027:LARIOH]2.0.CO;2> and Boose, Serrano, 
    and Foster (2004) <doi:10.1890/02-4057>.
	"""
	
	homepage = "https://github.com/hurrecon-model/HurreconR"
	cran = "HurreconR" 

	version("1.1", md5="4247949298d726eda14f85d757c2586d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
