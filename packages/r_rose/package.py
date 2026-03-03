# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRose(RPackage):
	"""Random Over-Sampling Examples

	Functions to deal with binary classification
  problems in the presence of imbalanced classes. Synthetic balanced samples are  
  generated according to ROSE (Menardi and Torelli, 2013).  
  Functions that implement more traditional remedies to the class imbalance
  are also provided, as well as different metrics to evaluate a learner accuracy.
  These are estimated by holdout, bootstrap or cross-validation methods. 
	"""
	
	cran = "ROSE" 

	version("0.0-4", md5="73db406449aae225ad8580e309fb433b")

