# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntervalaverage(RPackage):
	"""Time-Weighted Averaging for Interval Data

	Perform fast and memory efficient time-weighted averaging of values 
    measured over intervals into new arbitrary intervals. 
	This package is useful in the context of data measured or represented
	as constant values over intervals on a one-dimensional discrete axis 
	(e.g. time-integrated averages of a curve over defined periods). 
	This package was written specifically to deal with air 
	pollution data recorded or predicted as averages over sampling periods. 
	Data in this format often needs to be shifted to non-aligned periods 
	or averaged up to periods of longer duration (e.g. averaging data measured over 
	sequential non-overlapping periods to calendar years). 
	"""
	
	cran = "intervalaverage" 

	version("0.8.0", md5="2041978b9856e4139234bf4567ba8fb8")

	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
