# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGifski(RPackage):
	"""Highest Quality GIF Encoder

	Multi-threaded GIF encoder written in Rust: <https://gif.ski/>. 
    Converts images to GIF animations using pngquant's efficient cross-frame 
    palettes and temporal dithering with thousands of colors per frame.
	"""
	
	homepage = "https://r-rust.r-universe.dev/gifski"
	cran = "gifski" 

	version("1.12.0-2", md5="b132e35042ef99534d06d6bd6242a0ca")

	depends_on("rust", type=("build", "link", "run"))
