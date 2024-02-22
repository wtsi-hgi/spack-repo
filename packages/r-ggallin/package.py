# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgallin(RPackage):
	"""Grab Bag of 'ggplot2' Functions

	Extra geoms and scales for 'ggplot2', including geom_cloud(),
  a Normal density cloud replacement for errorbars;
  transforms ssqrt_trans and pseudolog10_trans, which are loglike but 
  appropriate for negative data; interp_trans() and warp_trans() which
  provide scale transforms based on interpolation;
  and an infix compose operator for scale transforms.
	"""
	
	homepage = "https://github.com/shabbychef/ggallin"
	cran = "ggallin" 

	version("0.1.1", md5="451a2787b14cde14c19b96acdab48e10")

	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
