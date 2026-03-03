# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNhpoisson(RPackage):
	"""Modelling and Validation of Non Homogeneous Poisson Processes

	Tools for modelling, ML estimation, validation analysis and simulation of non homogeneous Poisson processes in time. 
	"""
	
	cran = "NHPoisson" 

	version("3.3", md5="505216f300c1c155ec4a9ddb25373f2b")

	depends_on("r-car", type=("build", "run"))
