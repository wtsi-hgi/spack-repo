# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBst(RPackage):
	"""Gradient Boosting

	Functional gradient descent algorithm for a variety of convex and non-convex loss functions, for both classical and robust regression and classification problems. See Wang (2011) <doi:10.2202/1557-4679.1304>, Wang (2012) <doi:10.3414/ME11-02-0020>, Wang (2018) <doi:10.1080/10618600.2018.1424635>, Wang (2018) <doi:10.1214/18-EJS1404>.
	"""
	
	cran = "bst" 

	version("0.3-24", md5="6e89fbc98002fd63d5529392c19f561d")

	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
