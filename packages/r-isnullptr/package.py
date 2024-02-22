# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsnullptr(RPackage):
	"""Check if an 'externalptr' is a Null Pointer

	
    Check if an 'externalptr' is a null pointer.
    R does currently not have a native function for that purpose.
    This package contains a C function that returns TRUE in case of a null pointer.
	"""
	
	cran = "isnullptr" 

	version("1.0.1", md5="ea2ed0d93a0278fa3c0bac407ef244eb")

	depends_on("r@3:", type=("build", "run"))
