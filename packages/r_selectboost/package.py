# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelectboost(RPackage):
	"""A General Algorithm to Enhance the Performance of Variable
Selection Methods in Correlated Datasets

	An implementation of the selectboost algorithm (Bertrand et al. 2020, 'Bioinformatics', <doi:10.1093/bioinformatics/btaa855>), which is a general algorithm that improves the precision of any existing variable selection method. This algorithm is based on highly intensive simulations and takes into account the correlation structure of the data. It can either produce a confidence index for variable selection or it can be used in an experimental design planning perspective.
	"""
	
	homepage = "https://fbertran.github.io/SelectBoost/"
	cran = "SelectBoost" 

	version("2.2.2", md5="f653358b3bae708bc2ffe64ba57fe488")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-msgps", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-cascade", type=("build", "run"))
	depends_on("r-varbvs", type=("build", "run"))
	depends_on("r-spls", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
