# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCfacoop(RPackage):
	"""Colony Formation Assay: Taking into Account Cellular Cooperation

	Cellular cooperation compromises the plating efficiency-based 
    analysis of clonogenic survival data. This tool provides functions that 
    enable a robust analysis of colony formation assay (CFA) data in presence 
    or absence of cellular cooperation. 
    The implemented method has been described 
    in Brix et al. (2020). (Brix, N., Samaga, D., Hennel, R. et al. 
    "The clonogenic assay: robustness of plating efficiency-based analysis is 
    strongly compromised by cellular cooperation." Radiat Oncol 15, 248 (2020).
    <doi:10.1186/s13014-020-01697-y>)
        Power regression for parameter estimation, calculation of survival
    fractions, uncertainty analysis and plotting functions are provided.
	"""
	
	homepage = "https://github.com/ZytoHMGU/CFAcoop"
	cran = "CFAcoop" 

	version("1.0.0", md5="96c3eb9c8e6959892e3227455efd648c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
