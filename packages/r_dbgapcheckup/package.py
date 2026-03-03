# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbgapcheckup(RPackage):
	"""dbGaP Checkup

	Contains functions that check for formatting of the Subject Phenotype data set and data dictionary as specified by the National Center for Biotechnology Information (NCBI) Database of Genotypes and Phenotypes (dbGaP) <https://www.ncbi.nlm.nih.gov/gap/docs/submissionguide/>. 
	"""
	
	homepage = "https://lwheinsberg.github.io/dbGaPCheckup/"
	cran = "dbGaPCheckup" 

	version("1.1.0", md5="4e91f719e0591c4a4d89fb110b6411ae")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-questionr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-naniar", type=("build", "run"))
