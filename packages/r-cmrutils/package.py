# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmrutils(RPackage):
	"""Misc Functions of the Center for Mathematical Research

	A collection of useful helper routines developed by
  students of the Center for Mathematical Research, Stankin,
  Moscow.
	"""
	
	homepage = "https://github.com/aparamon/cmrutils"
	cran = "cmrutils" 

	version("1.3.1", md5="0048eb4321be7559c77cbe969a79e5fa")

	depends_on("r-chron", type=("build", "run"))
