# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhotobiologysun(RPackage):
	"""Data for Sunlight Spectra

	Data for the extraterrestrial solar spectral irradiance and ground 
    level solar spectral irradiance and irradiance. In addition data for 
    shade light under vegetation and irradiance time series from different
    broadband sensors.  Part of the 
    'r4photobiology' suite, Aphalo P. J. (2015) <doi:10.19232/uv4pb.2015.1.14>.
	"""
	
	homepage = "http://www.r4photobiology.info"
	cran = "photobiologySun" 

	version("0.5.0", md5="dcd0b673c00600f386a38acb76479192")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-photobiology@0.11.2:", type=("build", "run"))
