# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgm2(RPackage):
	"""Nested Resolvable Designs and their Associated Uniform Designs

	Construction method of nested resolvable designs from 
    a projective geometry defined on Galois field of order 2. The obtained
    Resolvable designs are used to build uniform design. The presented results
    are based on <https://eudml.org/doc/219563> and A. Boudraa et al. (See references).
	"""
	
	homepage = "<https://sites.google.com/site/mohamedlaibwebpage/"
	cran = "PGM2" 

	version("1.0-1", md5="9ea75749ec9998da73774138df279544", url="https://cran.r-project.org/src/contrib/PGM2_1.0-1.tar.gz")

