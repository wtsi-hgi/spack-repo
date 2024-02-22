# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUkbCovid19(RPackage):
	"""UK Biobank COVID-19 Data Processing and Risk Factor Association
Tests

	Process UK Biobank COVID-19 test result data for susceptibility, severity and mortality analyses, perform potential non-genetic COVID-19 risk factor and co-morbidity association tests. Wang et al. (2021) <doi:10.5281/zenodo.5174381>.
	"""
	
	homepage = "https://github.com/bahlolab/UKB.COVID19"
	cran = "UKB.COVID19" 

	version("0.1.4", md5="d0cf0d7de201ad8e81239b118bbac926", url="https://cran.r-project.org/src/contrib/UKB.COVID19_0.1.4.tar.gz")

	depends_on("r-questionr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
