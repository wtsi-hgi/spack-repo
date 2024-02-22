# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefer(RPackage):
	"""Create Object References

	Allows users to easily create references to R objects then
    'dereference' when needed or modify in place without using reference 
    classes, environments, or active bindings as workarounds. Users can 
    also create expression references that allow subsets of any object to 
    be referenced or expressions containing references to multiple 
    objects.
	"""
	
	cran = "refer" 

	version("0.1.0", md5="e3788f6a943851eab09a044995d4caa8")

	depends_on("r-elist", type=("build", "run"))
	depends_on("r-matchr", type=("build", "run"))
