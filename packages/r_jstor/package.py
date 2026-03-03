# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJstor(RPackage):
	"""Read Data from JSTOR/DfR

	Functions and helpers to import metadata, ngrams and full-texts 
    delivered by Data for Research by JSTOR. 
	"""
	
	homepage = "https://github.com/ropensci/jstor"
	cran = "jstor" 

	version("0.3.11", md5="ffe3d9ca1b36e19ad6423df2ab24340f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@0.7.2:", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-xml2@1.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-readr@2:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-furrr@0.1:", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
