# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebp(RPackage):
	"""A New Format for Lossless and Lossy Image Compression

	Lossless webp images are 26% smaller in size compared to PNG. Lossy
    webp images are 25-34% smaller in size compared to JPEG. This package reads
    and writes webp images into a 3 (rgb) or 4 (rgba) channel bitmap array using
    conventions from the 'jpeg' and 'png' packages.
	"""
	
	homepage = "https://jeroen.r-universe.dev/webp"
	cran = "webp" 

	version("1.2.0", md5="27bab6a71a65ba34e5f3eacbbe03a635")

	depends_on("libwebp", type=("build", "link", "run"))
