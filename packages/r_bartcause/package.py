# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBartcause(RPackage):
	"""Causal Inference using Bayesian Additive Regression Trees

	Contains a variety of methods to generate typical causal inference estimates using Bayesian Additive Regression Trees (BART) as the underlying regression model (Hill (2012) <doi:10.1198/jcgs.2010.08162>).
	"""
	
	homepage = "https://github.com/vdorie/bartCause"
	cran = "bartCause" 

	version("1.0-6", md5="cb23559fb0a98232818d038db3f3c9cc")

	depends_on("r@3.1.0:", type=("build", "run"))
	depends_on("r-dbarts@0.9.16:", type=("build", "run"))
