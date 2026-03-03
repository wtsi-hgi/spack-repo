# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDr(RPackage):
	"""Methods for Dimension Reduction for Regression

	Functions, methods, and datasets for fitting dimension
 reduction regression, using slicing (methods SAVE and SIR), Principal
 Hessian Directions (phd, using residuals and the response), and an
 iterative IRE.  Partial methods, that condition on categorical
 predictors are also available.  A variety of tests, and stepwise
 deletion of predictors, is also included.  Also included is
 code for computing permutation tests of dimension.  Adding additional
 methods of estimating dimension is straightforward.
 For documentation, see the vignette in the package.   With version 3.0.4,
 the arguments for dr.step have been modified.
	"""
	
	homepage = "https://cran.r-project.org/package=dr"
	cran = "dr" 

	version("3.0.10", md5="c097f3a3cd1f0a911ccec777d89681e4")

	depends_on("r-mass", type=("build", "run"))
