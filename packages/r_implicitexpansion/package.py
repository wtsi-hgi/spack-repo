# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImplicitexpansion(RPackage):
	"""Array Operations for Arrays of Mismatching Sizes

	Support for implicit expansion of arrays in operations involving
    arrays of mismatching sizes. This pattern is known as "broadcasting" in
    'Python' and  "implicit expansion" in 'Matlab' and is explained for example in
    the article "Array programming with NumPy" by C. R. Harris et al. (2020)
    <doi:10.1038/s41586-020-2649-2>.
	"""
	
	homepage = "https://github.com/ManuelHentschel/implicitExpansion"
	cran = "implicitExpansion" 

	version("0.1.0", md5="cba8eb87972b7de949e8ca4cb50c1f6b")

