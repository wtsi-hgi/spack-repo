# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmtl(RPackage):
	"""Heterogeneous Multi-Task Feature Learning

	The heterogeneous multi-task feature learning is a data integration method to conduct joint feature selection across multiple related data sets with different distributions. The algorithm can combine different types of learning tasks, including linear regression, Huber regression, adaptive Huber, and logistic regression. The modified version of Bayesian Information Criterion (BIC) is produced to measure the model performance. Package is based on Yuan Zhong, Wei Xu, and Xin Gao (2022) <https://www.fields.utoronto.ca/talk-media/1/53/65/slides.pdf>.
	"""
	
	cran = "HMTL" 

	version("0.1.0", md5="509edb3ba773320ffbe1ae66e9e51dab")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
