# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIjtiff(RPackage):
	"""Comprehensive TIFF I/O with Full Support for 'ImageJ' TIFF Files

	General purpose TIFF file I/O for R users.  Currently the
    only such package with read and write support for TIFF files with
    floating point (real-numbered) pixels, and the only package that can
    correctly import TIFF files that were saved from 'ImageJ' and write
    TIFF files than can be correctly read by 'ImageJ'
    <https://imagej.net/ij/>. Also supports text image I/O.
	"""
	
	homepage = "https://docs.ropensci.org/ijtiff/"
	cran = "ijtiff" 

	version("2.3.4", md5="09d154c48233d3cb5d2a88f808248909")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate@1.9.3:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs@1.5:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-strex@1.5:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-withr@2.1:", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
	depends_on("libtiff", type=("build", "link", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("libdeflate", type=("build", "link", "run"))
	depends_on("libjpeg", type=("build", "link", "run"))
	depends_on("lzma", type=("build", "link", "run"))
	depends_on("libwebp", type=("build", "link", "run"))
	depends_on("zstd", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
