# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcdklibs(RPackage):
	"""The CDK Libraries Packaged for R

	An R interface to the Chemistry Development Kit, a Java library
    for chemoinformatics. Given the size of the library itself, this package is
    not expected to change very frequently. To make use of the CDK within R, it is
    suggested that you use the 'rcdk' package. Note that it is possible to directly
    interact with the CDK using 'rJava'. However 'rcdk' exposes functionality in a more
    idiomatic way. The CDK library itself is released as LGPL and the sources can be
    obtained from <https://github.com/cdk/cdk>.
	"""
	
	homepage = "https://cdk-r.github.io/rcdklibs/"
	cran = "rcdklibs" 

	version("2.9", md5="b1c063c63b02f714f0b3f01ed23ed93d")
	version("2.8", md5="b42330b0f70643371d07dc26178a9d8c")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
