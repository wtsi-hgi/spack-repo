# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyn(RPackage):
	"""Time Series Regression

	Time series regression.  The dyn class interfaces ts,
        irts(), zoo() and zooreg() time series classes to lm(), glm(),
        loess(), quantreg::rq(), MASS::rlm(), MCMCpack::MCMCregress(),
        quantreg::rq(), randomForest::randomForest() and other regression
        functions allowing those functions to be used with time series
        including specifications that may contain lags, diffs and
        missing values.
	"""
	
	cran = "dyn" 

	version("0.2-9.6", md5="460057cf0d711fd812557a1a8adefad4")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-zoo@1.0.0:", type=("build", "run"))
