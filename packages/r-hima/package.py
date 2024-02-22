# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHima(RPackage):
	"""High-Dimensional Mediation Analysis

	Allows to estimate and test high-dimensional mediation effects based on advanced mediator screening and penalized regression techniques. Methods used in the package refer to Zhang H, Zheng Y, Zhang Z, Gao T, Joyce B, Yoon G, Zhang W, Schwartz J, Just A, Colicino E, Vokonas P, Zhao L, Lv J, Baccarelli A, Hou L, Liu L. Estimating and Testing High-dimensional Mediation Effects in Epigenetic Studies. Bioinformatics. (2016) <doi:10.1093/bioinformatics/btw351>. PMID: 27357171.
	"""
	
	homepage = "https://github.com/YinanZheng/HIMA/"
	cran = "HIMA" 

	version("2.2.1", md5="7ee6704135802a46f01d0a8348027efd")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-hdmt", type=("build", "run"))
	depends_on("r-hdi", type=("build", "run"))
	depends_on("r-conquer", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-hommel", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
