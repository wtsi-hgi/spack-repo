# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChoroplethradmin1(RPackage):
	"""Contains an Administrative-Level-1 Map of the World

	Contains an administrative-level-1 map of the world.
    Administrative-level-1 is the generic term for the largest sub-national
    subdivision of a country. This package was created for use with the
    choroplethr package.
	"""
	
	homepage = "http://www.arilamstein.com/open-source"
	cran = "choroplethrAdmin1" 

	version("1.1.1", md5="86f4078710a8f30a8ab1af6d6fb71831", url="https://cran.r-project.org/src/contrib/choroplethrAdmin1_1.1.1.tar.gz")

	depends_on("r-ggplot2", type=("build", "run"))
