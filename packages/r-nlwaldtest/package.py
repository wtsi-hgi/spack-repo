# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlwaldtest(RPackage):
	"""Wald Test of Nonlinear Restrictions and Nonlinear CI

	Wald Test for nonlinear restrictions on model parameters and confidence
             intervals for nonlinear functions  of parameters using delta-method.  Applicable
             after ANY model, provided parameters estimates and their covariance matrix are
             available.
	"""
	
	cran = "nlWaldTest" 

	version("1.1.3", md5="5410737548d52f104622acd610e90b01")

	depends_on("r@3.0.2:", type=("build", "run"))
