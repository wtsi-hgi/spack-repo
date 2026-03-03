# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatrprofile(RPackage):
	"""Column Profile for Tables and Datasets

	Profiles datasets (collecting statistics and informative summaries 
    about that data) on data frames and 'ODBC' tables: maximum, minimum, mean, standard deviation, nulls,
    distinct values, data patterns, data/format frequencies.
	"""
	
	homepage = "https://github.com/avitaliano/datrProfile"
	cran = "datrProfile" 

	version("0.1.0", md5="f2b34dc1a1a83751ec94ba6b80a273ba")

	depends_on("r-odbc", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
