# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlcm(RPackage):
	"""Calculate Textures from Grey-Level Co-Occurrence Matrices
(GLCMs)

	Enables calculation of image textures (Haralick 1973) 
    <doi:10.1109/TSMC.1973.4309314> from grey-level co-occurrence matrices 
    (GLCMs). Supports processing images that cannot fit in memory.
	"""
	
	homepage = "http://www.azvoleff.com/glcm"
	cran = "glcm" 

	version("1.6.5", md5="c8c4cf07a764faa994c99f29a61cc913")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
