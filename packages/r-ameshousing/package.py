# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmeshousing(RPackage):
	"""The Ames Iowa Housing Data

	Raw and processed versions of the data from De Cock (2011) <http://ww2.amstat.org/publications/jse> are included in the package. 
	"""
	
	homepage = "https://github.com/topepo/AmesHousing"
	cran = "AmesHousing" 

	version("0.0.4", md5="a25c1ab9116850fc9a4818a755ae641a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
