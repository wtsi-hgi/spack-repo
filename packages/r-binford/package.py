# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinford(RPackage):
	"""Binford's Hunter-Gatherer Data

	Binford's hunter-gatherer data includes more than 200 variables
    coding aspects of hunter-gatherer subsistence, mobility, and social organization
    for 339 ethnographically documented groups of hunter-gatherers.
	"""
	
	homepage = "http://github.com/benmarwick/binford"
	cran = "binford" 

	version("0.1.0", md5="666e430791fbe0053e3520b30f77be8d")

	depends_on("r@3.1:", type=("build", "run"))
