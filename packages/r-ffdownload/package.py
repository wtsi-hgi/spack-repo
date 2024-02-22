# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFfdownload(RPackage):
	"""Download Data from Kenneth French's Website

	Downloads all the datasets (you can exclude the daily ones or specify a list of those you are targeting specifically) from Kenneth French's Website at <https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html>, process them and convert them to list of 'xts' (time series).
	"""
	
	homepage = "https://github.com/sstoeckl/ffdownload"
	cran = "FFdownload" 

	version("1.1.1", md5="39c1dbb0a0ad6665229d2c18376f7377")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-timetk", type=("build", "run"))
