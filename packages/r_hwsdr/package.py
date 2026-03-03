# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHwsdr(RPackage):
	"""Interface to the 'HWSD' Web Services

	Programmatic interface to the Harmonized World Soil Database 
    'HWSD' web services (<https://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=1247>).
    Allows for easy downloads of 'HWSD' soil data directly to your R workspace 
    or your computer. Routines for both single pixel data downloads and
    gridded data are provided.
	"""
	
	homepage = "https://github.com/bluegreen-labs/hwsdr"
	cran = "hwsdr" 

	version("1.1", md5="9b391eb07dc44e7398bf4e7eb0366f03")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
