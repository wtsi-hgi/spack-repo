# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmetlite(RPackage):
	"""Read and Write SMET Files

	Simple class to hold contents of a SMET file as specified in
    Bavay (2021) <https://code.wsl.ch/snow-models/meteoio/-/blob/master/doc/SMET_specifications.pdf>.
    There numerical meteorological measurements are all based on MKS (SI) units
    and timestamp is standardized to UTC time. 
	"""
	
	homepage = "https://github.com/BaselDataScience/smetlite"
	cran = "smetlite" 

	version("0.2.10", md5="8ebb6b21daea7f9786e7d91e113d091d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
