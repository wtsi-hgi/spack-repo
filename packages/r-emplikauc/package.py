# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmplikauc(RPackage):
	"""Empirical Likelihood Ratio Test/Confidence Interval for AUC or
pAUC

	Test hypotheses and construct confidence intervals for AUC (area under Receiver 
             Operating Characteristic curve) and pAUC (partial area under ROC curve), from the
			 given two samples of test data with disease/healthy subjects. The method used is
			 based on two sample empirical likelihood, as described in
			 <https://www.ms.uky.edu/~mai/research/eAUC1.pdf>.		 
	"""
	
	cran = "emplikAUC" 

	version("0.3", md5="f6a0b35dd4beddf76821450cf0282f08")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-emplik2", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
