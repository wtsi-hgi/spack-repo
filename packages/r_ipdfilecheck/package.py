# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpdfilecheck(RPackage):
	"""Basic Functions to Check Readability, Consistency, and Content
of an Individual Participant Data File

	Basic checks needed with an individual level participant data from randomised controlled trial. This 
    checks files for existence, read access and individual columns for formats. The checks on format is currently implemented for gender and age formats. 
	"""
	
	cran = "IPDFileCheck" 

	version("0.8.1", md5="5105b3887db125bc3e7dc0b591411a9f")
	version("0.7.5", md5="d33d2a263d52af0ea4e3e2008e7c2ae6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-eeptools", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-gtsummary", type=("build", "run"))
	depends_on("r-effsize", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
