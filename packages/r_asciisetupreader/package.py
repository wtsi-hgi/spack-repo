# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsciisetupreader(RPackage):
	"""Reads Fixed-Width ASCII Data Files (.txt or .dat) that Have
Accompanying Setup Files (.sps or .sas)

	Lets you open a fixed-width ASCII file (.txt or
    .dat) that has an accompanying setup file (.sps or .sas). These file
    combinations are sometimes referred to as .txt+.sps, .txt+.sas,
    .dat+.sps, or .dat+.sas. This will only run in a txt-sps or txt-sas
    pair in which the setup file contains instructions to open that text
    file. It will NOT open other text files, .sav, .sas, or .por data
    files. Fixed-width ASCII files with setup files are common in older
    (pre-2000) government data.
	"""
	
	homepage = "https://github.com/jacobkap/asciiSetupReader"
	cran = "asciiSetupReader" 

	version("2.5.1", md5="91fa106fa63cffc50ac13df0ed529a4a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-shiny@0.13:", type=("build", "run"))
	depends_on("r-miniui@0.1.1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.5:", type=("build", "run"))
