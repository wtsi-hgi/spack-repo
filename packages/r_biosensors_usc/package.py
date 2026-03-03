# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiosensorsUsc(RPackage):
	"""Distributional Data Analysis Techniques for Biosensor Data

	Unified and user-friendly framework for using new 
             distributional representations of biosensors data in different statistical modeling 
             tasks: regression models, hypothesis testing, cluster analysis, visualization, and 
             descriptive analysis. Distributional representations are a functional extension of 
             compositional time-range metrics and we have used them successfully so far in modeling 
             glucose profiles and accelerometer data. However, these functional representations can 
             be used to represent any biosensor data such as ECG or medical imaging such as fMRI.
             Matabuena M, Petersen A, Vidal JC, Gude F. "Glucodensities: A new representation of 
             glucose profiles using distributional data analysis" (2021) 
             <doi:10.1177/0962280221998064>.
	"""
	
	cran = "biosensors.usc" 

	version("1.0", md5="0a9bc8c9e4df922e5640f4b48c4c6b92")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-fda-usc", type=("build", "run"))
	depends_on("r-paralleldist", type=("build", "run"))
	depends_on("r-osqp", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
