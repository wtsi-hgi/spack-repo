# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGparotatedf(RPackage):
	"""Derivative Free Gradient Projection Factor Rotation

	Derivative Free Gradient Projection Algorithms for Factor Rotation.
    For more details see ?GPArotateDF. Theory for these functions can be found in
    the following publications:
    Jennrich (2004) <doi:10.1007/BF02295647>.
    Bernaards and Jennrich (2005) <doi:10.1177/0013164404272507>.
	"""
	
	cran = "GPArotateDF" 

	version("2023.11-1", md5="b7af42ab5470d93b54ab4e76f4350ee5")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
