# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArs(RPackage):
	"""Adaptive Rejection Sampling

	Adaptive Rejection Sampling, Original version.
	"""
	
	cran = "ars" 

	version("0.6", md5="b7d66a955e1977720b9d95de8ad125a1")

	depends_on("r@3.1.2:", type=("build", "run"))
