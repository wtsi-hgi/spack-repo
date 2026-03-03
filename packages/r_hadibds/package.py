# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHadibds(RPackage):
	"""Incomplete Block Designs using Hadamard Matrix (HadIBDs)

	Hadamard matrix based statistical designs are of immense importance as the resultant designs carry various desirable characterizing properties. Constructing Partially Balanced Incomplete Block Designs (PBIBds) using Kronecker product of incidence matrices of Balanced Incomplete Block (BIB) and Partially Balanced Incomplete Block (PBIB) designs is much evident from literature. Here, we have constructed Incomplete Block Designs (IBDs) based on Hadamard matrices and Kronecker product of Hadamard matrices.
	"""
	
	cran = "HadIBDs" 

	version("1.0.0", md5="cd4529191c65e14e779adb5786e16a02")

