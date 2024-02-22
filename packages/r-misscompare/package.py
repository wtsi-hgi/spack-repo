# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMisscompare(RPackage):
	"""Intuitive Missing Data Imputation Framework

	Offers a convenient pipeline to test and compare various missing data
  imputation algorithms on simulated and real data. These include simpler methods, such as mean and median
  imputation and random replacement, but also include more sophisticated algorithms already implemented in popular 
  R packages, such as 'mi', described by Su et al. (2011) <doi:10.18637/jss.v045.i02>; 'mice', described by van Buuren 
  and Groothuis-Oudshoorn (2011) <doi:10.18637/jss.v045.i03>; 'missForest', described by Stekhoven and Buhlmann (2012) 
  <doi:10.1093/bioinformatics/btr597>; 'missMDA', described by Josse and Husson (2016) <doi:10.18637/jss.v070.i01>; and 
  'pcaMethods', described by Stacklies et al. (2007) <doi:10.1093/bioinformatics/btm069>. The central assumption behind 
  'missCompare' is that structurally different datasets (e.g. larger datasets with a large number of correlated variables 
  vs. smaller datasets with non correlated variables) will benefit differently from different missing data imputation 
  algorithms. 'missCompare' takes measurements of your dataset and sets up a sandbox to try a curated list of standard and 
  sophisticated missing data imputation algorithms and compares them assuming custom missingness patterns.
  'missCompare' will also impute your real-life dataset for you after the selection of the best performing algorithm
  in the simulations. The package also provides various post-imputation diagnostics and visualizations to help you 
  assess imputation performance.   
	"""
	
	cran = "missCompare" 

	version("1.0.3", md5="f06d0f47bd5f8addbd9001045e4bdb23")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-amelia", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mi", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-missmda", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vim", type=("build", "run"))
