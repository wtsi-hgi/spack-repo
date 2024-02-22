# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColorpatch(RPackage):
	"""Optimized Rendering of Fold Changes and Confidence Values

	Shows color patches for encoding fold changes (e.g. log ratios) together with confidence values 
    within a single diagram. This is especially useful for rendering gene expression data as well as
    other types of differential experiments. In addition to different rendering methods (ggplot extensions)
    functionality for perceptually optimizing color palettes are provided.
    Furthermore the package provides extension methods of the colorspace color-class in order to
    simplify the work with palettes (a.o. length, as.list, and append are supported).
	"""
	
	homepage = "http://sysbio.uni-ulm.de/?Software:colorpatch"
	cran = "colorpatch" 

	version("0.1.2", md5="b3e6a63a1ac0dd547e7209c89d3e9dd6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-tsp", type=("build", "run"))
