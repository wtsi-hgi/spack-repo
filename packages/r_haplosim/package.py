# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage
from spack.package import *


class RHaplosim(RPackage):
	"""Functions to Simulate Haplotypes

	Simulate haplotypes through meioses. Allows specification
        of population parameters.
	"""
	
	cran = "HaploSim" 

	version("1.8.4.2", md5="5e37ee0ed87231d02689653b9db421f6")
