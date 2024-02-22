# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwcvp(RPackage):
	"""Generating Summaries, Reports and Plots from the World Checklist
of Vascular Plants

	A companion to the World Checklist of 
    Vascular Plants (WCVP). It includes functions to generate maps and species lists, as 
    well as match names to the WCVP. For more details and to cite the package, see: 
    Brown M.J.M., Walker B.E., Black N., Govaerts R., Ondo I., Turner R., Nic Lughadha E. (in press). 
    "rWCVP: A companion R package to the World Checklist of Vascular Plants". New Phytologist.
	"""
	
	homepage = "https://github.com/matildabrown/rWCVP"
	cran = "rWCVP" 

	version("1.2.4", md5="8c92d2d9f0069ad0df405fef3ec646dc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-phonics", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-recordlinkage", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
