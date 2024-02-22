# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConnectednessapproach(RPackage):
	"""Connectedness Approach

	The estimation of static and dynamic connectedness measures is created in a modular and user-friendly way. Besides, the time domain connectedness approaches, this package further allows to estimate the frequency connectedness approach, the joint spillover index and the extended joint connectedness approach. In addition, all connectedness frameworks can be based upon orthogonalized and generalized VAR, QVAR, LASSO VAR, Ridge VAR, Elastic Net VAR and TVP-VAR models. Furthermore, the package includes the conditional, decomposed and partial connectedness measures as well as the pairwise connectedness index, influence index and corrected total connectedness index. Finally, a battery of datasets are available allowing to replicate a variety of connectedness papers.
	"""
	
	cran = "ConnectednessApproach" 

	version("1.0.1", md5="464202b5b4c8c4dcd8b2dd120126bee9")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-frequencyconnectedness", type=("build", "run"))
	depends_on("r-rmgarch", type=("build", "run"))
	depends_on("r-rugarch", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-riskparityportfolio", type=("build", "run"))
