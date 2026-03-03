# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParqr(RPackage):
	"""Read in Multi-Part Parquet Files

	Reads in multi-part parquet files. Will read in parquet files that have not been previously coalesced into one file. Convenient for reading in moderately sized, but split files. 
	"""
	
	homepage = "https://github.com/jhnwllr/parqr"
	cran = "parqr" 

	version("0.1.0", md5="29b88f15a08d5818fd94be9f538e0f69")

	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
