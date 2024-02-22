# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRforestry(RPackage):
	"""Random Forests, Linear Trees, and Gradient Boosting for
Inference and Interpretability

	Provides fast implementations of Honest Random Forests, 
    Gradient Boosting, and Linear Random Forests, with an emphasis on inference 
    and interpretability. Additionally contains methods for variable 
    importance, out-of-bag prediction, regression monotonicity, and
    several methods for missing data imputation. Soren R. Kunzel, 
    Theo F. Saarinen, Edward W. Liu, Jasjeet S. Sekhon (2019) <arXiv:1906.06463>.
	"""
	
	homepage = "https://github.com/forestry-labs/Rforestry"
	cran = "Rforestry" 

	version("0.10.0", md5="c080ce8324879ffe46d823aacab0900a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-glmnet@4.1:", type=("build", "run"))
	depends_on("r-onehot", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
