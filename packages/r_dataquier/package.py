# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataquier(RPackage):
	"""Data Quality in Epidemiological Research

	Data quality assessments guided by a
    'data quality framework introduced by Schmidt and colleagues, 2021' 
    <doi:10.1186/s12874-021-01252-7> target the
    data quality dimensions integrity, completeness, consistency, and
    accuracy. The scope of applicable functions rests on the
    availability of extensive metadata which can be provided in
    spreadsheet tables. Either standardized (e.g. as 'html5' reports) or
    individually tailored reports can be generated. For an introduction
    into the specification of corresponding metadata, please refer to the
    'package website'
    <https://dataquality.qihs.uni-greifswald.de/Annotation_of_Metadata.html>.
	"""
	
	homepage = "https://dataquality.qihs.uni-greifswald.de/"
	cran = "dataquieR" 

	version("2.1.0", md5="6954a5b4c2a31894e014dc75ef26f1a2")
	version("2.0.1", md5="bc56fd66ea12fea9943c2a4699d1c693")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-ggplot2@3.5:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-multinomialci", type=("build", "run"))
	depends_on("r-parallelmap", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-r-devices", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-qmrparser", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
