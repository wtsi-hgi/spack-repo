# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoar(RPackage):
	"""Memory management in R by delayed assignments

	Allows objects to be stored on disc and automatically
       		recalled into memory, as required, by delayed assignment.
	"""
	
	cran = "SOAR" 

	version("0.99-11", md5="3788baddd46d2cc8563247942b2af17f")

	depends_on("r@2.9:", type=("build", "run"))
