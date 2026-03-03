# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistrom(RPackage):
	"""Distributed Multinomial Regression

	Fast distributed/parallel estimation for multinomial logistic regression via Poisson factorization and the 'gamlr' package.  For details see: Taddy (2015, AoAS), Distributed Multinomial Regression, <arXiv:1311.6139>.
	"""
	
	homepage = "https://github.com/TaddyLab/distrom"
	cran = "distrom" 

	version("1.0.1", md5="ab6aa64494a384c4a821db00795d63ed")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gamlr", type=("build", "run"))
