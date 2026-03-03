# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCustomderivative(RPackage):
	"""Pricing Various Types of Custom Derivatives

	A versatile R package for creating and pricing custom derivatives to suit your financial needs.
	"""
	
	cran = "CustomDerivative" 

	version("0.1.1", md5="dcba67a8097cc2bae001f3bd5510e5e2")

	depends_on("r-r6", type=("build", "run"))
