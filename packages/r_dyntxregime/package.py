# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyntxregime(RPackage):
	"""Methods for Estimating Optimal Dynamic Treatment Regimes

	Methods to estimate dynamic treatment regimes using Interactive
  Q-Learning, Q-Learning, weighted learning, and value-search methods based on 
  Augmented Inverse Probability Weighted Estimators and Inverse Probability
  Weighted Estimators. Dynamic Treatment Regimes: Statistical Methods for 
  Precision Medicine, Tsiatis, A. A., Davidian, M. D., Holloway, S. T., and Laber, E. B., 
  Chapman & Hall/CRC Press, 2020, ISBN:978-1-4987-6977-8.
	"""
	
	cran = "DynTxRegime" 

	version("4.15", md5="7b906a9bdc417415e4ee6d67968e23af")

	depends_on("r-modelobj", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
	depends_on("r-dfoptim", type=("build", "run"))
