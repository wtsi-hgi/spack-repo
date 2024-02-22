# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidymultiqc(RPackage):
	"""Converts 'MultiQC' Reports into Tidy Data Frames

	Provides the means to convert 'multiqc_data.json' files,
    produced by the wonderful 'MultiQC' tool, into tidy data frames for downstream
    analysis in R. This analysis might involve cohort analysis, quality control visualisation,
    change-point detection, statistical process control, clustering, or any other
    type of quality analysis.
	"""
	
	homepage = "https://multimeric.github.io/TidyMultiqc/"
	cran = "TidyMultiqc" 

	version("1.0.3", md5="2b350c1b2cbab4708ad16902dbeab4f2")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
