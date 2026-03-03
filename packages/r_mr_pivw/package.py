# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrPivw(RPackage):
	"""Penalized Inverse-Variance Weighted Estimator for Mendelian
Randomization

	The penalized inverse-variance weighted (pIVW) estimator is a Mendelian randomization method for estimating the causal effect of an exposure variable on an outcome of interest based on summary-level GWAS data. The pIVW estimator accounts for weak instruments and balanced horizontal pleiotropy simultaneously. See Xu S., Wang P., Fung W.K. and Liu Z. (2022) <doi:10.1111/biom.13732>.  
	"""
	
	cran = "mr.pivw" 

	version("0.1.1", md5="4f94258017028f6b3b248145388e63f7")

	depends_on("r@3.5:", type=("build", "run"))
