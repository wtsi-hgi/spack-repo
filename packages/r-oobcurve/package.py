# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROobcurve(RPackage):
	"""Out of Bag Learning Curve

	Provides functions to calculate the out-of-bag learning curve for random forests for any measure that is available in the 'mlr' package. Supported random forest packages are 'randomForest' and 'ranger' and trained models of these packages with the train function of 'mlr'. The main function is OOBCurve() that calculates the out-of-bag curve depending on the number of trees. With the OOBCurvePars() function out-of-bag curves can also be calculated for 'mtry', 'sample.fraction' and 'min.node.size' for the 'ranger' package.
	"""
	
	homepage = "https://github.com/PhilippPro/OOBCurve"
	cran = "OOBCurve" 

	version("0.3", md5="07b2c0c0061def5a9dbbd83b4b09dbb6")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-mlr@2.11:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
