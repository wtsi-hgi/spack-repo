# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStreammetabolism(RPackage):
	"""Calculate Single Station Metabolism from Diurnal Oxygen Curves

	I provide functions to calculate Gross Primary Productivity, Net Ecosystem Production, and Ecosystem Respiration from single station diurnal Oxygen curves.  
	"""
	
	homepage = "https://github.com/ssefick/StreamMetabolism"
	cran = "StreamMetabolism" 

	version("1.1.3", md5="b5799745b88613b5c8d7c9d03a171c4d")

	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-suntools", type=("build", "run"))
