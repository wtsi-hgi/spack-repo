# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaterialmodifier(RPackage):
	"""Apply Photo Editing Effects

	You can apply image processing effects that modifies the perceived material properties of objects
    in photos, such as gloss, smoothness, and blemishes. This is an implementation of the algorithm proposed by
    Boyadzhiev et al. (2015) "Band-Sifting Decomposition for Image Based Material Editing".
    Documentation and practical tips of the package is available at <https://github.com/tsuda16k/materialmodifier>.
	"""
	
	homepage = "https://github.com/tsuda16k/materialmodifier"
	cran = "materialmodifier" 

	version("1.2.0", md5="f05d20961f7064f038ab0b6f4cf50204")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-readbitmap", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
