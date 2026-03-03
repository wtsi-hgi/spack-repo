# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcmwfr(RPackage):
	"""Interface to 'ECMWF' and 'CDS' Data Web Services

	Programmatic interface to the European Centre for Medium-Range
    Weather Forecasts dataset web services (ECMWF; <https://www.ecmwf.int/>)
    and Copernicus's Climate Data Store (CDS; 
    <https://cds.climate.copernicus.eu>). Allows for easy downloads of weather 
    forecasts and climate reanalysis data in R.
	"""
	
	homepage = "https://github.com/bluegreen-labs/ecmwfr"
	cran = "ecmwfr" 

	version("1.5.0", md5="b89379a41ac217247b7b6697112fcf60")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
