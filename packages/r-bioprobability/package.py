# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioprobability(RPackage):
	"""Probability in Biostatistics

	Several tools for analyzing diagnostic tests and 2x2 contingency tables are provided. In particular, positive and negative predictive values for a diagnostic tests can be calculated from prevalence, sensitivity and specificity values. For contingency tables, relative risk and odds ratio measures are estimated. Furthermore, confidence intervals are provided. 
	"""
	
	cran = "BioProbability" 

	version("1.0", md5="0d023e41890ef83da14026238f3b5eb1")

