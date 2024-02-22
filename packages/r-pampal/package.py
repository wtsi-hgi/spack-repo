# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPampal(RPackage):
	"""Load and Process Passive Acoustic Data

	Tools for loading and processing passive acoustic data. Read in data
    that has been processed in 'Pamguard' (<https://www.pamguard.org/>), apply a suite
    processing functions, and export data for reports or external modeling tools. Parameter 
    calculations implement methods by Oswald et al (2007) <doi:10.1121/1.2743157>,
    Griffiths et al (2020) <doi:10.1121/10.0001229> and Baumann-Pickering et al (2010)
    <doi:10.1121/1.3479549>.
	"""
	
	cran = "PAMpal" 

	version("1.0.0", md5="17436a7367ad9c7d6be41ddbf9920555")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pambinaries@1.3:", type=("build", "run"))
	depends_on("r-pammisc@1.8.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-seewave", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-manipulate", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
