# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRamlegacy(RPackage):
	"""Download and Read RAM Legacy Stock Assessment Database

	Contains functions to download, cache and read in 'Excel' version of the
    RAM Legacy Stock Assessment Data Base, an online compilation of stock assessment
    results for commercially exploited marine populations from around the world. 
    The database is named after Dr. Ransom A. Myers whose original stock-recruitment database,
    is no longer being updated. More information about the database can be found at
    <https://ramlegacy.org/>. Ricard, D., Minto, C., Jensen, O.P. and Baum, J.K. (2012) <doi:10.1111/j.1467-2979.2011.00435.x>.
	"""
	
	homepage = "https://github.com/ropensci/ramlegacy"
	cran = "ramlegacy" 

	version("0.2.0", md5="e5a65332dbd06a38704c893618f669ee")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli@1:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-rappdirs@0.3.1:", type=("build", "run"))
	depends_on("r-readxl@1.1:", type=("build", "run"))
