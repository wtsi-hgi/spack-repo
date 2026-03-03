# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvaluatecore(RPackage):
	"""Quality Evaluation of Core Collections

	Implements various quality evaluation statistics to assess the
    value of plant germplasm core collections using qualitative and 
    quantitative phenotypic trait data according to Odong et al. (2015) 
    <doi:10.1007/s00122-012-1971-y>.
	"""
	
	homepage = "https://github.com/aravind-j/EvaluateCore"
	cran = "EvaluateCore" 

	version("0.1.3", md5="4944b0f4d825a4925b722d298702d652")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-agricolae", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-ggcorrplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ksamples", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
