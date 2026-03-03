# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtable(RPackage):
	"""Generation of Perturbation Tables for the Cell-Key Method

	Tabular data from statistical institutes and agencies are mostly 
    confidential and must be protected prior to publications. The cell-key 
    method is a post-tabular Statistical Disclosure Control perturbation 
    technique that adds random noise to tabular data. The statistical 
    properties of the perturbations are defined by some noise probability 
    distributions - also referred to as perturbation tables. 
    This tool can be used to create the perturbation tables based on a maximum 
    entropy approach as described for example in Giessing (2016) 
    <doi:10.1007/978-3-319-45381-1_18>. The perturbation tables created can 
    finally be used to apply a cell-key method to frequency count or magnitude 
    tables.
	"""
	
	homepage = "https://github.com/sdcTools/ptable"
	cran = "ptable" 

	version("1.0.0", md5="3134d78ddb2eeafdd1199a8843b584a0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-flexdashboard", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
