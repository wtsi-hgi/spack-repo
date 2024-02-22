# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFabricatr(RPackage):
	"""Imagine Your Data Before You Collect It

	Helps you imagine your data before you collect it. Hierarchical data structures
   and correlated data can be easily simulated, either from random number generators or
   by resampling from existing data sources. This package is faster with 'data.table' and
   'mvnfast' installed.
	"""
	
	homepage = "https://declaredesign.org/r/fabricatr/"
	cran = "fabricatr" 

	version("1.0.2", md5="d0e4c325160f22c0b8697a66906b35ea")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
