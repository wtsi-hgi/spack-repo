# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsm(RPackage):
	"""Gamma Shape Mixture

	Implementation of a Bayesian approach for estimating a mixture of gamma distributions in which the mixing occurs over the shape parameter. This family provides a flexible and novel approach for modeling heavy-tailed distributions, it is computationally efficient, and it only requires to specify a prior distribution for a single parameter.
	"""
	
	homepage = "http://projecteuclid.org/euclid.aoas/1215118537"
	cran = "GSM" 

	version("1.3.2", md5="5305b6932e5b7c2907da18baf8a556a6")

	depends_on("r-gtools", type=("build", "run"))
