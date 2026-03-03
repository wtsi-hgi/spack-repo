# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDocore(RPackage):
	"""Utility Functions for Scientific Coding

	Basic routines used in scientific coding, such as timing routines, vector/array handing functions and I/O support routines.
	"""
	
	cran = "docore" 

	version("1.0", md5="c9c5f9e5f100d10c5a4ff68059d40a4f")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
