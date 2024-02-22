# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExposr(RPackage):
	"""Models Topographic Exposure to Hurricane Winds

	The EXPOS model uses a digital elevation model (DEM) to estimate
    exposed and protected areas for a given hurricane wind direction and
    inflection angle. The resulting topographic exposure maps can be combined
    with output from the HURRECON model to estimate hurricane wind damage
    across a region. For details on the original version of the EXPOS model
    written in 'Borland Pascal', see: Boose, Foster, and Fluet (1994)
    <doi:10.2307/2937142>, Boose, Chamberlin, and Foster (2001)
    <doi:10.1890/0012-9615(2001)071[0027:LARIOH]2.0.CO;2>, and Boose,
    Serrano, and Foster (2004) <doi:10.1890/02-4057>.
	"""
	
	homepage = "https://github.com/expos-model/ExposR"
	cran = "ExposR" 

	version("1.1", md5="c435c5cff199f04104902e153327badf")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
