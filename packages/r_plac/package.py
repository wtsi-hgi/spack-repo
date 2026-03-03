# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlac(RPackage):
	"""A Pairwise Likelihood Augmented Cox Estimator for Left-Truncated
Data

	A semi-parametric estimation method for the Cox model
    with left-truncated data using augmented information
    from the marginal of truncation times.
	"""
	
	homepage = "https://github.com/942kid/plac"
	cran = "plac" 

	version("0.1.3", md5="df0598062e4f3de99ce0bf35aba16bcd")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-survival@2.38.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
