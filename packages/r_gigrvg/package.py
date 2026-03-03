# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGigrvg(RPackage):
	"""Random Variate Generator for the GIG Distribution

	
  Generator and density function for the
  Generalized Inverse Gaussian (GIG) distribution.
	"""
	
	cran = "GIGrvg" 

	version("0.8", md5="83d80c24c95406c55f61c48aea888960")

