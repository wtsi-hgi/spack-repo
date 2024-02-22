# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamclass(RPackage):
	"""Functions and Data for a Course on Modern Regression and
Classification

	Functions and data are provided that support a course
        that emphasizes statistical issues of inference and generalizability.  
        The functions are designed to make it straightforward to illustrate
        the use of cross-validation, the training/test approach, simulation, 
        and model-based estimates of accuracy.  Methods considered are
        Generalized Additive Modeling, Linear and Quadratic Discriminant
        Analysis, Tree-based methods, and Random Forests. 
	"""
	
	cran = "gamclass" 

	version("0.62.5", md5="b955b13ad369a35dbacfbf57c13e137a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
