# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmix(RPackage):
	"""Variable Selection in Linear Mixed Models for SNP Data

	Fit penalized multivariable linear mixed models with a single 
    random effect to control for population structure in genetic association 
    studies. The goal is to simultaneously fit many genetic variants at the 
    same time, in order to select markers that are independently associated 
    with the response. Can also handle prior annotation information, 
    for example, rare variants, in the form of variable weights. For more 
    information, see the website below and the accompanying paper: 
    Bhatnagar et al., "Simultaneous SNP selection and adjustment for 
    population structure in high dimensional prediction models", 2020, 
    <DOI:10.1371/journal.pgen.1008766>.
	"""
	
	homepage = "https://github.com/sahirbhatnagar/ggmix"
	cran = "ggmix" 

	version("0.0.2", md5="a04d1b12ad67a75b9ab94be74f8544ff")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
