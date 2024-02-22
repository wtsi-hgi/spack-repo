# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdrsampsize(RPackage):
	"""Compute Sample Size that Meets Requirements for Average Power
and FDR

	Defines a collection of functions to compute average power and sample size for studies that use the false discovery rate as the final measure of statistical significance.
	"""
	
	cran = "FDRsampsize" 

	version("1.0", md5="b7fb6572fc4a4d11c588b5e49a1430e9")

	depends_on("r@2.15.1:", type=("build", "run"))
