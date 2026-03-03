# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPyramid(RPackage):
	"""Draw Population Pyramid

	Drawing population pyramid using (1) data.frame or (2) vectors.
	 The former is named as pyramid() and the latter pyramids(), as wrapper
	 function of pyramid().  pyramidf() is the function to draw population
	 pyramid within the specified frame.
	"""
	
	homepage = "http://minato.sip21c.org/swtips/Rgraphics.html#PYRAMID"
	cran = "pyramid" 

	version("1.5", md5="899a8a3dad4d952f63ec9701ae7933b0")

	depends_on("r@2.2:", type=("build", "run"))
