# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFact(RPackage):
	"""Feature Attributions for ClusTering

	We present 'FACT' (Feature Attributions for ClusTering), a
  framework for unsupervised interpretation methods that can be used with an 
  arbitrary clustering algorithm. The package is capable of re-assigning instances to
  clusters (algorithm agnostic), preserves the integrity of the data and does
  not introduce additional models. 'FACT' is inspired by the principles of
  model-agnostic interpretation in supervised learning. Therefore, some of the
  methods presented are based on 'iml', a R Package for Interpretable Machine
  Learning by Christoph Molnar, Giuseppe Casalicchio, and Bernd Bischl (2018)
  <doi:10.21105/joss.00786>.
	"""
	
	cran = "FACT" 

	version("0.1.0", md5="8570227015f797de3cc0b5d84ed5f461")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-prediction", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-iml", type=("build", "run"))
