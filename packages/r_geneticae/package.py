# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneticae(RPackage):
	"""Statistical Tools for the Analysis of Multi Environment
Agronomic Trials

	Data from multi environment agronomic trials, which are often 
  carried out by plant breeders, can be analyzed with the tools offered by this 
  package such as the Additive Main effects and Multiplicative Interaction model 
  or 'AMMI' ('Gauch' 1992, ISBN:9780444892409) 
  and the Site Regression model or 'SREG' ('Cornelius' 1996, 
  <doi:10.1201/9780367802226>). Since these methods present a poor performance 
  under the presence of outliers and missing values, this package includes 
  robust versions of the 'AMMI' model ('Rodrigues' 2016, 
  <doi:10.1093/bioinformatics/btv533>), and also imputation techniques 
  specifically developed for this kind of data ('Arciniegas-Alarcón' 2014, 
  <doi:10.2478/bile-2014-0006>).
	"""
	
	homepage = "https://jangelini.github.io/geneticae/"
	cran = "geneticae" 

	version("0.4.0", md5="18dca9b7fbe185485f9ddc374394476a")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-ggebiplots", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-missmda", type=("build", "run"))
	depends_on("r-calibrate", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-prettydoc", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
