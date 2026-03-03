# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDplyrassist(RPackage):
	"""RStudio Addin for Teaching and Learning Data Manipulation Using
'dplyr'

	An RStudio addin for teaching and learning data manipulation using the 'dplyr' package.
    You can learn each steps of data manipulation by clicking your mouse without coding.
    You can get resultant data (as a 'tibble') and the code for data manipulation.
	"""
	
	homepage = "https://github.com/cardiomoon/dplyrAssist"
	cran = "dplyrAssist" 

	version("0.1.0", md5="7907e051fd97f2739136b6e7895536b9")

	depends_on("r-shiny@0.13:", type=("build", "run"))
	depends_on("r-miniui@0.1.1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.5:", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
