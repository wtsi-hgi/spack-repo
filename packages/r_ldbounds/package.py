# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdbounds(RPackage):
	"""Lan-DeMets Method for Group Sequential Boundaries

	Computations related to group sequential boundaries.
    Includes calculation of bounds using the Lan-DeMets
    alpha spending function approach. Based on FORTRAN
        program ld98 implemented by Reboussin, et al. (2000) <doi:10.1016/s0197-2456(00)00057-x>.
	"""
	
	cran = "ldbounds" 

	version("2.0.2", md5="5560df90ba9f5d693721a29afbfe62df")

