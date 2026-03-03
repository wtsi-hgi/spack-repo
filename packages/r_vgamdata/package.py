# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVgamdata(RPackage):
	"""Data Supporting the 'VGAM' Package

	Mainly data sets to accompany the VGAM package and
	the book "Vector Generalized Linear and
	Additive Models: With an Implementation in R" (Yee, 2015)
	<DOI:10.1007/978-1-4939-2818-7>.
	These are used to illustrate vector generalized
	linear and additive models (VGLMs/VGAMs), and associated models
	(Reduced-Rank VGLMs, Quadratic RR-VGLMs, Row-Column
	Interaction Models, and constrained and unconstrained ordination
	models in ecology). This package now contains some
	old VGAM family functions which have been replaced by newer
	ones (often because they are now special cases).
	"""
	
	homepage = "https://www.stat.auckland.ac.nz/~yee/VGAMdata/"
	cran = "VGAMdata" 

	version("1.1-9", md5="a5bce93331a85c63ccd49069392cbb82")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
