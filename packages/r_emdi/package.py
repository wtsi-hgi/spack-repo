# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmdi(RPackage):
	"""Estimating and Mapping Disaggregated Indicators

	Functions that support estimating, assessing and mapping regional
    disaggregated indicators. So far, estimation methods comprise direct estimation,
    the model-based unit-level approach Empirical Best Prediction (see "Small area
    estimation of poverty indicators" by Molina and Rao (2010) <doi:10.1002/cjs.10051>), 
    the area-level model (see "Estimates of income for small places: An 
    application of James-Stein procedures to Census Data" by Fay and Herriot (1979) 
    <doi:10.1080/01621459.1979.10482505>) and various extensions of it (adjusted variance 
    estimation methods, log and arcsin transformation, spatial, robust and measurement 
    error models), as well as their precision estimates. The assessment of the used model
    is supported by a summary and diagnostic plots. For a suitable presentation of
    estimates, map plots can be easily created. Furthermore, results can easily be
    exported to excel. For a detailed description of the package and the methods used
    see "The R Package emdi for Estimating and Mapping Regionally Disaggregated Indicators" 
    by Kreutzmann et al. (2019) <doi:10.18637/jss.v091.i07> and the second package vignette 
    "A Framework for Producing Small Area Estimates Based on Area-Level Models in R".
	"""
	
	homepage = "https://github.com/SoerenPannier/emdi"
	cran = "emdi" 

	version("2.2.1", md5="f82dc49c124ef709ce53f021f13a87b2")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mumin", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-parallelmap", type=("build", "run"))
	depends_on("r-hlmdiag", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-readods", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-saerobust", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
