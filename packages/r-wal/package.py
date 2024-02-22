# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWal(RPackage):
	"""Read and Write 'wal' Bitmap Image Files and Other 'Quake' Assets

	Read 'Quake' assets including bitmap images and textures in 'wal' file format. This package also provides support for extracting these assets from 'WAD' and 'PAK' file archives. It can also read models in 'MDL' and 'MD2' formats.
	"""
	
	homepage = "https://github.com/dfsp-spirit/wal"
	cran = "wal" 

	version("0.1.1", md5="59dc30c0683420476e84bf1b023b9cf3")

	depends_on("r-freesurferformats@0.1.12:", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-spacesxyz", type=("build", "run"))
