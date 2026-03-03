# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImputeree(RPackage):
	"""Impute Missing Rare Earth Element Data in Zircon

	Set of functions to impute missing rare earth data, calculate La 
    and Pr concentrations and Ce anomalies in zircons based on the
    Chondrite-Onuma and Chondrite-Lattice of Carrasco-Godoy and 
    Campbell (2023) <doi:10.1007/s00410-023-02025-9> and the Logarithmic regression from  
    Zhong et al. (2019) <doi:10.1007/s00710-019-00682-y>.
	"""
	
	homepage = "https://github.com/cicarrascog/imputeREE"
	cran = "imputeREE" 

	version("0.0.5", md5="2ff4cd134c612cf814c692402b2d5227")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
