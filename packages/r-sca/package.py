# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSca(RPackage):
	"""Simple Component Analysis

	Simple Component Analysis (SCA) often provides much more
   interpretable components than Principal Components (PCA) while still
   representing much of the variability in the data.
	"""
	
	cran = "sca" 

	version("0.9-2", md5="968ed920daa6fd4cdd12e2ebdbbbe8f6")

