# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActivityindex(RPackage):
	"""Activity Index Calculation using Raw 'Accelerometry' Data

	Reads raw 'accelerometry' from 'GT3X+' data and 
    plain table data to calculate Activity Index from 'Bai et al.' (2016)
    <doi:10.1371/journal.pone.0160644>.  The Activity Index refers to the 
    square root of the second-level average variance of the three
    'accelerometry' axes.
	"""
	
	cran = "ActivityIndex" 

	version("0.3.7", md5="2a292e3eaef18840caeb39eb04188286")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
