# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfcca(RPackage):
	"""Random Forest with Canonical Correlation Analysis

	Random Forest with Canonical Correlation Analysis (RFCCA) is a 
  random forest method for estimating the canonical correlations between two 
  sets of variables depending on the subject-related covariates. The trees are 
  built with a splitting rule specifically designed to partition the data to 
  maximize the canonical correlation heterogeneity between child nodes. The 
  method is described in Alakus et al. (2021) <doi:10.1093/bioinformatics/btab158>. 
  'RFCCA' uses 'randomForestSRC' package (Ishwaran and Kogalur, 2020) by 
  freezing at the version 2.9.3. The custom splitting rule feature is utilised 
  to apply the proposed splitting rule. The 'randomForestSRC' package implements 
  'OpenMP' by default, contingent upon the support provided by the target 
  architecture and operating system. In this package, 'LAPACK' and 'BLAS' 
  libraries are used for matrix decompositions.
	"""
	
	homepage = "https://github.com/calakus/RFCCA"
	cran = "RFCCA" 

	version("2.0.0", md5="f5ee946fe4683741999eefa7ffaf52de")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cca", type=("build", "run"))
	depends_on("r-pma", type=("build", "run"))
