# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvr(RPackage):
	"""Mean-Variance Regularization

	This is a non-parametric method for joint adaptive mean-variance regularization and variance stabilization of high-dimensional data. It is suited for handling difficult problems posed by high-dimensional multivariate datasets (p >> n paradigm). Among those are that the variance is often a function of the mean, variable-specific estimators of variances are not reliable, and tests statistics have low powers due to a lack of degrees of freedom. Key features include:
            (i) Normalization and/or variance stabilization of the data,
            (ii) Computation of mean-variance-regularized t-statistics (F-statistics to follow),
            (iii) Generation of diverse diagnostic plots,
            (iv) Computationally efficient implementation using C/C++ interfacing and an option for parallel computing to enjoy a faster and easier experience in the R environment.
	"""
	
	homepage = "https://github.com/jedazard/MVR"
	cran = "MVR" 

	version("1.33.0", md5="510285f4ee42d22f34e6cccb8da81e71")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
