# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromer(RPackage):
	"""Interface to Chromosome Counts Database API

	A programmatic interface to the Chromosome Counts Database
    (<https://ccdb.tau.ac.il/>), Rice et al. (2014) <doi:10.1111/nph.13191>.
    This package is part of the 'ROpenSci' suite (<https://ropensci.org>).
	"""
	
	homepage = "https://docs.ropensci.org/chromer/"
	cran = "chromer" 

	version("0.6", md5="cea260774067121c2917319a953a7ad1")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
