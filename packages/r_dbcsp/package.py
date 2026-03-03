# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbcsp(RPackage):
	"""Distance-Based Common Spatial Patterns

	A way to apply Distance-Based Common Spatial Patterns
    (DB-CSP) techniques in different fields, both classical Common Spatial
    Patterns (CSP) as well as DB-CSP. The method is composed of two
    phases: applying the DB-CSP algorithm and performing a classification.
    The main idea behind the CSP is to use a linear transform to project
    data into low-dimensional subspace with a projection matrix, in such a
    way that each row consists of weights for signals. This transformation
    maximizes the variance of two-class signal matrices.The dbcsp object
    is created to compute the projection vectors. For exploratory and
    descriptive purpose, plot and boxplot functions can be used. Functions
    train, predict and selectQ are implemented for the classification
    step.
	"""
	
	cran = "dbcsp" 

	version("0.0.2.1", md5="4236d88747481bc6cb432ee350c8e37c")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tsdist@3.7:", type=("build", "run"))
	depends_on("r-geigen", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-paralleldist", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
