# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMissinghandle(RPackage):
	"""Handles Missing Dates and Data and Converts into Weekly and
Monthly from Daily

	Many times, you will not find data for all dates. After first January, 2011 you may have next data on 20th January, 2011 and so on. Also available dates may have zero values. Try to gather all such kinds of data in different excel sheets of a single excel file. Every sheet will contain two columns (1st one is dates and second one is the data). After loading all the sheets into different elements of a list, using this you can fill the gaps for all the sheets and mark all the corresponding values as zeros. Here I am talking about daily data. Finally, it will combine all the filled results into one data frame (first column is date and other columns will be corresponding values of your sheets) and give one combined data frame. Number of columns in the data frame will be number of sheets plus one. Then imputation will be done. Daily to monthly and weekly conversion is also possible.  More details can be found in Garai and others (2023) <doi:10.13140/RG.2.2.11977.42087>.
	"""
	
	cran = "MissingHandle" 

	version("0.1.1", md5="7c44b20bd2f971b200e151d338a81824")

	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-imputets", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
