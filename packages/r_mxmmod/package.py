# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMxmmod(RPackage):
	"""Measurement Model of Derivatives in 'OpenMx'

	Provides a convenient interface in 'OpenMx' for building
    Estabrook's (2015) <doi:10.1037/a0034523> Measurement Model of
    Derivatives (MMOD).
	"""
	
	cran = "mxmmod" 

	version("1.1.0", md5="c6d4357438ad561c16dcb0854f63eeec")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-openmx", type=("build", "run"))
