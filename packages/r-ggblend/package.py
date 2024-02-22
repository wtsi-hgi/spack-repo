# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgblend(RPackage):
	"""Blending and Compositing Algebra for 'ggplot2'

	Algebra of operations for blending, copying, adjusting, and 
    compositing layers in 'ggplot2'. Supports copying and adjusting the 
    aesthetics or parameters of an existing layer, partitioning a layer 
    into multiple pieces for re-composition, applying affine transformations
    to layers, and combining layers (or partitions of layers) using blend modes
    (including commutative blend modes, like multiply and darken). Blend 
    mode support is particularly useful for creating plots with overlapping 
    groups where the layer drawing order does not change the output; 
    see Kindlmann and Scheidegger (2014) <doi:10.1109/TVCG.2014.2346325>.
	"""
	
	homepage = "https://mjskay.github.io/ggblend/"
	cran = "ggblend" 

	version("0.1.0", md5="bef691b931d22a3fad215d4eacd3dd38")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
