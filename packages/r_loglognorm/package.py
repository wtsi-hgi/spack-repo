# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoglognorm(RPackage):
	"""Double Log Normal Distribution Functions

	Functions to sample from the double log normal distribution and calculate the density, distribution and quantile functions.
	"""
	
	cran = "loglognorm" 

	version("1.0.2", md5="bf74205cca86919be11f193e5fbb4f1a")

	depends_on("r@4.1:", type=("build", "run"))
