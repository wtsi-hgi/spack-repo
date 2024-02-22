# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogisticrci(RPackage):
	"""Linear and Logistic Regression-Based Reliable Change Index

	Here we provide an implementation of the linear and logistic regression-based Reliable Change Index (RCI), to be used with lm and binomial glm model objects, respectively, following Moral et al. <https://psyarxiv.com/gq7az/>. The RCI function returns a score assumed to be approximately normally distributed, which is helpful to detect patients that may present cognitive decline.
	"""
	
	cran = "LogisticRCI" 

	version("1.1", md5="61ebd031402ae89dda59e2d13dd60c74")

	depends_on("r@3.6:", type=("build", "run"))
