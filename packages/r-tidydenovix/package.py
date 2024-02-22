# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidydenovix(RPackage):
	"""Cleans Spectrophotometry Data Obtained from the Denovix DS-11
Instrument

	Cleans spectrophotometry data obtained from the Denovix instrument. The package also provides an option to normalize the data in order to compare the quality of the samples obtained.
	"""
	
	homepage = "https://github.com/AlphaPrime7/tidyDenovix"
	cran = "tidyDenovix" 

	version("2.1.0", md5="1d52dd6ea7c6f4fffb960c0561bb4d48")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
