# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRetroharmonize(RPackage):
	"""Ex Post Survey Data Harmonization

	Assist in reproducible retrospective (ex-post) harmonization
    of data, particularly individual level survey data, by providing tools
    for organizing metadata, standardizing the coding of variables, and
    variable names and value labels, including missing values, and
    documenting the data transformations, with the help of comprehensive
    s3 classes.
	"""
	
	homepage = "https://retroharmonize.dataobservatory.eu/"
	cran = "retroharmonize" 

	version("0.2.0", md5="894156e843b4c17e56fb05f02e0c0ef0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
