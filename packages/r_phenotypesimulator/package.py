# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenotypesimulator(RPackage):
	"""Flexible Phenotype Simulation from Different Genetic and Noise
Models

	Simulation is a critical part of method development and assessment
    in quantitative genetics. 'PhenotypeSimulator' allows for the flexible 
    simulation of phenotypes under different models, including genetic variant 
    and  infinitesimal genetic effects (reflecting population structure) as well 
    as non-genetic covariate effects, observational noise and additional 
    correlation effects. The different phenotype components are combined into a 
    final phenotype while controlling for the proportion of variance explained 
    by each of the components. For each effect component, the number of 
    variables, their distribution and the design of their effect across traits 
    can be customised. For the simulation of the genetic effects, external 
    genotype data from a number of standard software ('plink', 'hapgen2'/
    'impute2', 'genome', 'bimbam', simple text files) can be imported. The final 
    simulated phenotypes and its components can be automatically saved into .rds 
    or .csv files. In addition, they can be saved in formats compatible with 
    commonly used genetic association software ('gemma', 'bimbam', 'plink', 
    'snptest', 'LiMMBo'). 
	"""
	
	homepage = "https://github.com/HannahVMeyer/PhenotypeSimulator"
	cran = "PhenotypeSimulator" 

	version("0.3.4", md5="7053f85727f1065a4c7c1015f38808d0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-optparse", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-snpstats", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-data-table@1.11:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
