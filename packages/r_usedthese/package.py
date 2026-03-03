# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsedthese(RPackage):
	"""Summarises Package & Function Usage

	Consistent with 'knitr' syntax highlighting, 'usedthese' adds a
    summary table of R package & function usage to a Quarto document and 
    enables aggregation of usage across a Quarto website. Learn more about
    'usedthese' at <https://cgoo4.github.io/usedthese/>.
	"""
	
	homepage = "https://cgoo4.github.io/usedthese/"
	cran = "usedthese" 

	version("0.3.3", md5="d70e4033bee0165ceb9401596198eaf0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-conflicted@1.2:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-highr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
