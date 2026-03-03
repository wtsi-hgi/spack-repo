# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdsc(RPackage):
	"""Time Domain Signal Coding

	Functions for performing time domain signal coding as used in Chesmore (2001) <doi:10.1016/S0003-682X(01)00009-3>, and related tasks. This package creates the standard S-matrix and A-matrix (with variable lag), has tools to convert coding matrices into distributed matrices, provides published codebooks and allows for extraction of code sequences.
	"""
	
	cran = "tdsc" 

	version("1.0.4", md5="10138a91601e6be1d2b83e09b4db01f7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
