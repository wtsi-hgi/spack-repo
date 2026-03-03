# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmonize(RPackage):
	"""Support Retrospective Harmonization of Data

	Functions to support rigorous retrospective data harmonization 
    processing, evaluation, and documentation across datasets from different 
    studies based on Maelstrom Research guidelines. The package includes the 
    core functions to evaluate and format the main inputs that define the 
    harmonization process, apply specified processing rules to generate 
    harmonized data, diagnose processing errors, and summarize and evaluate 
    harmonized outputs. The main inputs that define the processing are a 
    DataSchema (list and definitions of harmonized variables to be generated) 
    and Data Processing Elements (processing rules to be applied to generate 
    harmonized variables from study-specific variables). The main outputs of 
    processing are harmonized datasets, associated metadata, and tabular and 
    visual summary reports. As described in 
    Maelstrom Research guidelines for rigorous retrospective data 
    harmonization (Fortier I and al. (2017) <doi:10.1093/ije/dyw075>).
	"""
	
	homepage = "https://github.com/maelstrom-research/Rmonize/"
	cran = "Rmonize" 

	version("1.0.1", md5="621e60b34036c5013efa6fc369e7ba4a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-fabr@2:", type=("build", "run"))
	depends_on("r-madshapr", type=("build", "run"))
