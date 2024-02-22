# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTouch(RPackage):
	"""Tools of Utilization and Cost in Healthcare

	R implementation of the software tools developed in the H-CUP
    (Healthcare Cost and Utilization Project) <https://www.hcup-us.ahrq.gov>
    and AHRQ (Agency for Healthcare Research and Quality)
    <https://www.ahrq.gov>.  It currently contains functions for mapping ICD-9
    codes to the AHRQ comorbidity measures and translating ICD-9
    (resp. ICD-10) codes to ICD-10 (resp. ICD-9) codes based on GEM (General
    Equivalence Mappings) from CMS (Centers for Medicare and Medicaid
    Services).
	"""
	
	homepage = "https://github.com/wenjie2wang/touch"
	cran = "touch" 

	version("0.1-6", md5="2378531cca74dc560554cacc964e56a6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
