# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaussfacts(RPackage):
	"""The Greatest Mathematician Since Antiquity

	Display a random fact about Carl Friedrich Gauss
 based the on collection curated by Mike Cavers via the
 <http://gaussfacts.com> site.
	"""
	
	cran = "gaussfacts" 

	version("0.0.2", md5="4e5b23ff9119dedf7b5db1a0effa7607")

