# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForestplot(RPackage):
	"""Advanced Forest Plot Using 'grid' Graphics

	A forest plot that allows for
    multiple confidence intervals per row,
    custom fonts for each text element,
    custom confidence intervals,
    text mixed with expressions, and more.
    The aim is to extend the use of forest plots beyond meta-analyses.
    This is a more general version of the original 'rmeta' package's forestplot()
    function and relies heavily on the 'grid' package.
	"""
	
	homepage = "https://gforge.se/packages/"
	cran = "forestplot" 

	version("3.1.3", md5="849e4da2a7d540f966bd3f0fa03821cb")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
