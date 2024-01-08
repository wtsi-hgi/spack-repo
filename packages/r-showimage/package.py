# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RShowimage(RPackage):
	"""Show an Image on an 'R' Graphics Device

	Sometimes it is handy to be able to view an image file on an
    'R' graphics device. This package just does that. Currently it supports
    'PNG' files.
	"""
	
	homepage = "https://github.com/r-lib/showimage#readme"
	cran = "showimage" 

	version("1.0.0", md5="a1a531498c4fc439693222dff9cc8e02")

	depends_on("r-png", type=("build", "run"))
