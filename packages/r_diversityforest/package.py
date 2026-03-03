# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiversityforest(RPackage):
	"""Innovative Complex Split Procedures in Random Forests Through
Candidate Split Sampling

	Implements interaction forests [1], which are specific diversity forests and 
  the basic form of diversity forests that uses univariable, binary splitting [2].
  Interaction forests (IFs) are ensembles of decision trees that model quantitative and
  qualitative interaction effects using bivariable splitting. IFs come with the 
  Effect Importance Measure (EIM), which can be used to identify variable pairs that 
  feature quantitative and qualitative interaction effects with high predictive
  relevance. IFs and EIM focus on well interpretable forms of interactions.
  The package also offers plot functions for visualising the estimated forms of 
  interaction effects.
  Categorical, metric, and survival outcomes are supported.
  This is a fork of the R package 'ranger' (main author: Marvin N. Wright) that 
  implements random forests using an efficient C++  implementation.
  References:
  [1] Hornung, R. & Boulesteix, A.-L. (2022) Interaction Forests: Identifying and 
      exploiting interpretable quantitative and qualitative interaction effects.
	  Computational Statistics & Data Analysis 171:107460, <doi:10.1016/j.csda.2022.107460>.
  [2] Hornung, R. (2022) Diversity forests: Using split sampling to enable 
      innovative complex split procedures in random forests.
	  SN Computer Science 3(2):1, <doi:10.1007/s42979-021-00920-1>.
	"""
	
	cran = "diversityForest" 

	version("0.4.0", md5="73a8a08d30eb21acac72bcfb2441fed3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-sgeostat", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-mapgam", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
