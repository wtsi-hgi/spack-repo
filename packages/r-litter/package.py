# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLitter(RPackage):
	"""Litter Analysis

	Data sets on various litter types like beach litter, riverain
    litter, floating litter, and seafloor litter are rapidly growing. This 
    package offers a simple user interface to analyse these litter data in
    a consistent and reproducible way. It also provides functions to 
    facilitate several kinds of litter analysis, e.g., trend analysis, 
    power analysis, and baseline analysis. Under the hood, these functions 
    are also used by the user interface. See Schulz et al. (2019)
    <doi:10.1016/j.envpol.2019.02.030> for details. MS-Windows users are
    advised to run 'litteR' in 'RStudio'. See our vignette: Installation manual 
    for 'RStudio' and 'litteR'.
	"""
	
	cran = "litteR" 

	version("1.0.0", md5="9e54d7f382ea899c943c97057ab00860")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-fs@1.4.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-yaml@2.2.1:", type=("build", "run"))
	depends_on("r-rmarkdown@2.2:", type=("build", "run"))
