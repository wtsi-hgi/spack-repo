# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStochprofml(RPackage):
	"""Stochastic Profiling using Maximum Likelihood Estimation

	New Version of the R package originally accompanying the paper 
  "Parameterizing cell-to-cell regulatory heterogeneities via stochastic transcriptional profiles" 
  by Sameer S Bajikar, Christiane Fuchs, Andreas Roller, Fabian J Theis and Kevin A Janes 
  (PNAS 2014, 111(5), E626-635 <doi:10.1073/pnas.1311647111>). In this paper, we measure expression profiles 
  from small heterogeneous populations of cells, where each cell is assumed to be from a mixture of 
  lognormal distributions. We perform maximum likelihood estimation in order to infer the mixture ratio and 
  the parameters of these lognormal distributions from the cumulated expression measurements.
  The main difference of this new package version to the previous one is that it is now possible to use 
  different n's, i.e. a dataset where each tissue sample originates from a different number of cells.  
  We used this on pheno-seq data, see: Tirier, S.M., Park, J., Preusser, F. et al. Pheno-seq - linking visual 
  features and gene expression in 3D cell culture systems. Sci Rep 9, 12367 (2019) 
  <doi:10.1038/s41598-019-48771-4>).
	"""
	
	cran = "stochprofML" 

	version("2.0.3", md5="da5264728e49cf9d51991056e2cf09e5")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
