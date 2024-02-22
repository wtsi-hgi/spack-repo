# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAirqualityes(RPackage):
	"""Air Quality Measurements in Spain from 2011 to 2018

	These dataset contains daily quality air measurements in 
  Spain over a period of 18 years (from 2001 to 2018). The measurements refer to 
  several pollutants. These data are openly published by the Government of Spain.  
  The datasets were originally spread over a number of files and formats. Here, 
  the same information is contained in simple dataframe for convenience of 
  researches, journalists or general public. See the Spanish Government website 
  <http://www.miteco.gob.es/> for more information.
	"""
	
	homepage = "https://github.com/jdieramon/airqualityES"
	cran = "airqualityES" 

	version("1.0.0", md5="339bf7ba817961ab9e6ad233c7d23bd9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
