# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcca(RPackage):
	"""Multi-Category Classification Accuracy

	It contains six common multi-category classification accuracy evaluation measures.
 All of these measures could be found in Li and Ming (2019) <doi:10.1002/sim.8103>. Specifically,
 Hypervolume Under Manifold (HUM), described in
 Li and Fine (2008) <doi:10.1093/biostatistics/kxm050>.
 Correct Classification Percentage (CCP), Integrated Discrimination Improvement (IDI), Net Reclassification Improvement (NRI), R-Squared Value (RSQ), described in
 Li, Jiang and Fine (2013) <doi:10.1093/biostatistics/kxs047>.
 Polytomous Discrimination Index (PDI), described in
 Van Calster et al. (2012) <doi:10.1007/s10654-012-9733-3>.
 Li et al. (2018) <doi:10.1177/0962280217692830>.
 We described all these above measures and our mcca package in
 Li, Gao and D'Agostino (2019) <doi:10.1002/sim.8103>.
	"""
	
	homepage = "https://github.com/gaoming96/mcca"
	cran = "mcca" 

	version("0.7.0", md5="a126867786d4edfd5ad9fc41bef136de")

	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
