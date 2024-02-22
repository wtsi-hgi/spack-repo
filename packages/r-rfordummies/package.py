# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfordummies(RPackage):
	"""Code Examples to Accompany the Book "R for Dummies"

	Contains all the code examples in the book "R for Dummies" (2nd
    edition) by Andrie de Vries and Joris Meys. You can view the table of 
    contents as well as the sample code for each chapter.
	"""
	
	homepage = "https://rfordummies.com"
	cran = "rfordummies" 

	version("0.1.6", md5="10c09893c0e23eb5269a6c011de585b5")

