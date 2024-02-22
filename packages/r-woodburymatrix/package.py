# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWoodburymatrix(RPackage):
	"""Fast Matrix Operations via the Woodbury Matrix Identity

	A hierarchy of classes and methods for manipulating matrices formed implicitly from the sums of the inverses of other matrices, a situation commonly encountered in spatial statistics and related fields. Enables easy use of the Woodbury matrix identity and the matrix determinant lemma to allow computation (e.g., solving linear systems) without having to form the actual matrix. More information on the underlying linear algebra can be found in Harville, D. A. (1997) <doi:10.1007/b98818>.
	"""
	
	homepage = "https://github.com/mbertolacci/WoodburyMatrix"
	cran = "WoodburyMatrix" 

	version("0.0.3", md5="6c41a0ac5167600376f6025918f739cc")

	depends_on("r-matrix", type=("build", "run"))
