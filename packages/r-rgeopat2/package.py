# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgeopat2(RPackage):
	"""Additional Functions for 'GeoPAT' 2

	Supports analysis of spatial data processed with the 'GeoPAT' 2
    software <https://github.com/Nowosad/geopat2>. 
    Available features include creation of a grid based on the 'GeoPAT' 2
    grid header file and reading a 'GeoPAT' 2 text outputs.
	"""
	
	homepage = "https://github.com/Nowosad/rgeopat2"
	cran = "rgeopat2" 

	version("0.4.0", md5="03f77aebada5de22377bc854c58d00de", url="https://cran.r-project.org/src/contrib/rgeopat2_0.4.0.tar.gz")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
