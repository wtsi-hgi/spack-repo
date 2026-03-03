# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCragg(RPackage):
	"""Tests for Weak Instruments in R

	Implements Cragg-Donald (1993) <doi:10.1017/S0266466600007519> and Stock and Yogo (2005) <doi:10.1017/CBO9780511614491.006> tests for weak instruments in R.
	"""
	
	cran = "cragg" 

	version("0.0.1", md5="cded9880e7303ab25310722b5066db14")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-expm@0.999:", type=("build", "run"))
