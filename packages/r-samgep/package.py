# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamgep(RPackage):
	"""A Semi-Supervised Method for Prediction of Phenotype Event Times

	A novel semi-supervised machine learning algorithm to predict phenotype event times using Electronic Health Record (EHR) data.
	"""
	
	homepage = "https://github.com/celehs/SAMGEP"
	cran = "SAMGEP" 

	version("0.1.0-1", md5="867c7d46697176ade5710b567137f55b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
