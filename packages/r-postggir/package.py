# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPostggir(RPackage):
	"""Data Processing after Running 'GGIR' for Accelerometer Data

	Generate all necessary R/Rmd/shell files for data processing after running 'GGIR' (v2.4.0) for accelerometer data. In part 1, all csv files in the GGIR output directory were read, transformed and then merged. In part 2, the GGIR output files were checked and summarized in one excel sheet. In part 3, the merged data was cleaned according to the number of valid hours on each night and the number of valid days for each subject. In part 4, the cleaned activity data was imputed by the average Euclidean norm minus one (ENMO) over all the valid days for each subject. Finally, a comprehensive report of data processing was created using Rmarkdown, and the report includes few exploratory plots and multiple commonly used features extracted from minute level actigraphy data. 
	"""
	
	homepage = "https://github.com/dora201888/postGGIR"
	cran = "postGGIR" 

	version("2.4.0.2", md5="c37808c5ce322734c2da9cc3d91e426d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-refund", type=("build", "run"))
	depends_on("r-denseflmm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-ineq", type=("build", "run"))
	depends_on("r-cosinor", type=("build", "run"))
	depends_on("r-cosinor2", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-accelerometry", type=("build", "run"))
	depends_on("r-actcr", type=("build", "run"))
	depends_on("r-actfrag", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-ggir", type=("build", "run"))
