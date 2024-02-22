# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixssg(RPackage):
	"""Clustering Using Mixtures of Sub Gaussian Stable Distributions

	Developed for model-based clustering using the finite mixtures of skewed sub-Gaussian
              stable distributions developed by Teimouri (2022) <arXiv:2205.14067> and estimating
              parameters of the symmetric stable distribution within the Bayesian framework.
	"""
	
	cran = "mixSSG" 

	version("2.1.1", md5="f6533e58f7e107c49f117e5e48569b9d")

	depends_on("r@3.4.3:", type=("build", "run"))
	depends_on("r-ars", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
