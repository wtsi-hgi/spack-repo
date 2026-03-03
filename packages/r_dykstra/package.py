# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDykstra(RPackage):
	"""Quadratic Programming using Cyclic Projections

	Solves quadratic programming problems using Richard L. Dykstra's cyclic projection algorithm. Routine allows for a combination of equality and inequality constraints. See Dykstra (1983) <doi:10.1080/01621459.1983.10477029> for details.
	"""
	
	cran = "Dykstra" 

	version("1.0-0", md5="92a70848d9f8a8494041f8868ab650ae")

