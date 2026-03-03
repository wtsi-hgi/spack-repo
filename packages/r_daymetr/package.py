# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaymetr(RPackage):
	"""Interface to the 'Daymet' Web Services

	Programmatic interface to the 'Daymet' web services
    (<http://daymet.ornl.gov>). Allows for easy downloads of
    'Daymet' climate data directly to your R workspace or your computer.
    Routines for both single pixel data downloads and
    gridded (netCDF) data are provided.
	"""
	
	homepage = "https://github.com/bluegreen-labs/daymetr"
	cran = "daymetr" 

	version("1.7.1", md5="6020a59b5f86dc85d608a9e1a80552b3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
