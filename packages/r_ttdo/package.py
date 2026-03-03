# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTtdo(RPackage):
	"""Extend 'tinytest' with 'diffobj'

	The 'tinytest' package offers a light-weight zero-dependency unit-testing
 framework to which this package adds support of the 'diffobj' package for 'diff'-style
 comparison of R objects.
	"""
	
	homepage = "https://github.com/eddelbuettel/ttdo/"
	cran = "ttdo" 

	version("0.0.9", md5="83688bccde0fc6d4f5a76ad98994f7e3")

	depends_on("r-tinytest@1.4.1:", type=("build", "run"))
	depends_on("r-diffobj", type=("build", "run"))
