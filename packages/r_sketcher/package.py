# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSketcher(RPackage):
	"""Pencil Sketch Effect

	An implementation of image processing effects that convert a photo into a line drawing image. 
    For details, please refer to Tsuda, H. (2020). sketcher: An R package for converting a photo into a sketch style image. 
    <doi:10.31234/osf.io/svmw5>.
	"""
	
	homepage = "https://htsuda.net/sketcher/"
	cran = "sketcher" 

	version("0.1.3", md5="8ae4bb22d895699177c530cf594f64f5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-readbitmap", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
