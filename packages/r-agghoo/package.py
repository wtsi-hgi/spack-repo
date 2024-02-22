# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgghoo(RPackage):
	"""Aggregated Hold-Out Cross Validation

	The 'agghoo' procedure is an alternative to usual cross-validation.
    Instead of choosing the best model trained on V subsamples, it determines
    a winner model for each subsample, and then aggregates the V outputs.
    For the details, see "Aggregated hold-out" by Guillaume Maillard,
    Sylvain Arlot, Matthieu Lerasle (2021) <arXiv:1909.04890>
    published in Journal of Machine Learning Research 22(20):1--55.
	"""
	
	homepage = "https://git.auder.net/?p=agghoo.git"
	cran = "agghoo" 

	version("0.1-0", md5="87450f3c01596f02956aef14a4644763")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
