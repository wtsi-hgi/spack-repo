# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVared(RPackage):
	"""Variance Estimation using Difference-Based Methods

	Generating functions for both optimal and ordinary difference sequences, and the difference-based estimation functions.
	"""
	
	cran = "VarED" 

	version("1.0.0", md5="0b098f380096e5965c71a8952da2348a")

	depends_on("r@3.3:", type=("build", "run"))
