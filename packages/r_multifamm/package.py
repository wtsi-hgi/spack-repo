# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultifamm(RPackage):
	"""Multivariate Functional Additive Mixed Models

	An implementation for multivariate functional additive mixed
    models (multiFAMM), see Volkmann et al. (2021, <arXiv:2103.06606>). It builds on developed methods for univariate sparse 
    functional regression models and multivariate functional principal component
    analysis. This package contains the function to run a multiFAMM and some
    convenience functions useful when working with large models. An additional 
    package on GitHub contains more convenience functions to reproduce the 
    analyses of the corresponding paper 
    (<https://github.com/alexvolkmann/multifammPaper>).
	"""
	
	cran = "multifamm" 

	version("0.1.1", md5="644b62496524aaf93c66242aea53914f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fundata", type=("build", "run"))
	depends_on("r-mfpca@1.3.2:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-sparseflmm@0.3:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
