# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTigerhitter(RPackage):
	"""Pre-Process of Time Series Data Set in R

	Pre-process for discrete time series data set which is not continuous at the column
    of 'date'. Refilling records of missing 'date' and other columns to the hollow data set so that
    final data set is able to be dealt with time series analysis.
	"""
	
	homepage = "https://github.com/Willdata/tigerhitteR"
	cran = "tigerhitteR" 

	version("1.1.0", md5="66664d687b1d4887667059da2f99ff83")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-openxlsx@3:", type=("build", "run"))
	depends_on("r-zoo@1.7.13:", type=("build", "run"))
	depends_on("r-hmisc@3.17.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
