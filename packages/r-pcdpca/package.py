# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcdpca(RPackage):
	"""Dynamic Principal Components for Periodically Correlated
Functional Time Series

	Method extends multivariate and functional dynamic principal components
    to periodically correlated multivariate time series. This package allows you to
    compute true dynamic principal components in the presence of periodicity. 
    We follow implementation guidelines as described in Kidzinski, Kokoszka and
    Jouzdani (2017), in Principal component analysis of periodically correlated
    functional time series <arXiv:1612.00040>.
	"""
	
	cran = "pcdpca" 

	version("0.4", md5="f937a2b5e2cc305e3bbcf78d34042443")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-freqdom", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
