# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrotli(RPackage):
	"""A Compression Format Optimized for the Web

	A lossless compressed data format that uses a combination of the
    LZ77 algorithm and Huffman coding. Brotli is similar in speed to deflate (gzip)
    but offers more dense compression.
	"""
	
	homepage = "https://www.rfc-editor.org/rfc/rfc7932"
	cran = "brotli" 

	version("1.3.0", md5="0582187b005d30c5bd2e8c7ffcd48872")

