# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoostingdea(RPackage):
	"""A Boosting Approach to Data Envelopment Analysis

	Includes functions to estimate production frontiers 
    and make ideal output predictions in the Data Envelopment Analysis (DEA) 
    context using both standard models from DEA and Free Disposal Hull (FDH)
    and boosting techniques. In particular, EATBoosting (Guillen et al., 2023 
    <doi:10.1016/j.eswa.2022.119134>) and MARSBoosting. Moreover, the package 
    includes code for estimating several technical efficiency measures using 
    different models such as the input and output-oriented radial measures, the
    input and output-oriented Russell measures, the Directional Distance 
    Function (DDF), the Weighted Additive Measure (WAM) and the Slacks-Based 
    Measure (SBM).
	"""
	
	homepage = "https://github.com/itsmeryguillen/boostingDEA"
	cran = "boostingDEA" 

	version("0.1.0", md5="3341fcf4fef6016ff14b61526104abce")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
	depends_on("r-mlmetrics", type=("build", "run"))
