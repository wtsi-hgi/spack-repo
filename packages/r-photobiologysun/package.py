# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhotobiologysun(RPackage):
	"""Data for Sunlight Spectra

	Data for the extraterrestrial solar spectral irradiance and ground 
    level solar spectral irradiance and irradiance. In addition data for 
    shade light under vegetation and irradiance time series.  Part of the 
    'r4photobiology' suite, Aphalo P. J. (2015) <doi:10.19232/uv4pb.2015.1.14>.
	"""
	
	homepage = "http://www.r4photobiology.info"
	cran = "photobiologySun" 

	version("0.4.1", md5="0f1e1ef91ebcf0340c7177da10c39052")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-photobiology@0.9.26:", type=("build", "run"))
