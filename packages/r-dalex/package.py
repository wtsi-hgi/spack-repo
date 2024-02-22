# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDalex(RPackage):
	"""moDel Agnostic Language for Exploration and eXplanation

	Any unverified black box model is the path to failure. Opaqueness leads to distrust. 
  Distrust leads to ignoration. Ignoration leads to rejection. 
  DALEX package xrays any model and helps to explore and explain its behaviour.
  Machine Learning (ML) models are widely used and have various applications in classification 
  or regression. Models created with boosting, bagging, stacking or similar techniques are often
  used due to their high performance. But such black-box models usually lack direct interpretability.
  DALEX package contains various methods that help to understand the link between input variables 
  and model output. Implemented methods help to explore the model on the level of a single instance 
  as well as a level of the whole dataset.
  All model explainers are model agnostic and can be compared across different models.
  DALEX package is the cornerstone for 'DrWhy.AI' universe of packages for visual model exploration.
  Find more details in (Biecek 2018) <arXiv:1806.08915>.
	"""
	
	homepage = "https://modeloriented.github.io/DALEX/"
	cran = "DALEX" 

	version("2.4.3", md5="eb0756c65611440e8d9a11742d47472f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ibreakdown@1.3.1:", type=("build", "run"))
	depends_on("r-ingredients@2:", type=("build", "run"))
