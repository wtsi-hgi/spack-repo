# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFar(RPackage):
	"""Modelization for Functional AutoRegressive Processes

	Modelizations and previsions functions for
   Functional AutoRegressive processes using
   nonparametric methods: functional kernel,
   estimation of the covariance operator in
   a subspace, ...
	"""
	
	homepage = "https://github.com/Looping027/far"
	cran = "far" 

	version("0.6-6", md5="75a5e103c721e6a9aae6353007cbe3c5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
