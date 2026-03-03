# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtt(RPackage):
	"""Hypothesis Testing Tree

	A novel decision tree algorithm in the hypothesis testing framework. The algorithm examines the distribution difference between two child nodes over all possible binary partitions. The test statistic of the hypothesis testing is equivalent to the generalized energy distance, which enables the algorithm to be more powerful in detecting the complex structure, not only the mean difference. It is applicable for numeric, nominal, ordinal explanatory variables and the response in general metric space of strong negative type. The algorithm has superior performance compared to other tree models in type I error, power, prediction accuracy, and complexity.
	"""
	
	cran = "HTT" 

	version("0.1.2", md5="6943fcf40226ff606898908ba36e6569")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
