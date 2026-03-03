# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFairml(RPackage):
	"""Fair Models in Machine Learning

	Fair machine learning regression models which take sensitive attributes into account in
  model estimation. Currently implementing Komiyama et al. (2018) 
  <http://proceedings.mlr.press/v80/komiyama18a/komiyama18a.pdf>, Zafar et al.
  (2019) <https://www.jmlr.org/papers/volume20/18-262/18-262.pdf> and my own
  approach from Scutari, Panero and Proissl (2022)
  <https://link.springer.com/content/pdf/10.1007/s11222-022-10143-w.pdf>
  that uses ridge regression to enforce fairness.
	"""
	
	cran = "fairml" 

	version("0.8", md5="8835a8ac862790308b6901c6d250b3cd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
