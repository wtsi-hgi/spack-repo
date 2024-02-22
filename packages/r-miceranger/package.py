# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiceranger(RPackage):
	"""Multiple Imputation by Chained Equations with Random Forests

	Multiple Imputation has been shown to 
  be a flexible method to impute missing values by 
  Van Buuren (2007) <doi:10.1177/0962280206074463>. 
  Expanding on this, random forests have been shown 
  to be an accurate model by Stekhoven and Buhlmann 
  <arXiv:1105.0828> to impute missing values in datasets. 
  They have the added benefits of returning out of bag 
  error and variable importance estimates, as well as 
  being simple to run in parallel.
	"""
	
	homepage = "https://github.com/FarrellDay/miceRanger"
	cran = "miceRanger" 

	version("1.5.0", md5="dcedbf083e4a4f74e3ce7412eb551efe")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
