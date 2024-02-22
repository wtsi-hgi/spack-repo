# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBabel(RPackage):
	"""Ribosome Profiling Data Analysis

	Included here are babel routines for identifying unusual ribosome protected fragment counts given mRNA counts.
	"""
	
	cran = "babel" 

	version("0.3-0", md5="3a3bd668de7bf8f508b70fded934b0c5")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
