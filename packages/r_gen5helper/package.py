# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGen5helper(RPackage):
	"""Processing 'Gen5' 2.06 Exported Data

	A collection of functions for processing 'Gen5' 2.06 exported data.
    'Gen5' is an essential data analysis software for BioTek plate readers <https://www.biotek.com/products/software-robotics-software/gen5-microplate-reader-and-imager-software/>. This package contains functions for data cleaning, 
    modeling and plotting using exported data from 'Gen5' version 2.06. It exports
    technically correct data defined in (Edwin de Jonge and Mark van der Loo 
    (2013) <https://cran.r-project.org/doc/contrib/de_Jonge+van_der_Loo-Introduction_to_data_cleaning_with_R.pdf>) for customized analysis. It 
    contains Boltzmann fitting for general kinetic analysis.  
    See <https://www.github.com/yanxianUCSB/gen5helper> for more information,
    documentation and examples.
	"""
	
	cran = "gen5helper" 

	version("1.0.1", md5="e76b0f298d688f62f2ff2542b4ac965d")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-naturalsort", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
