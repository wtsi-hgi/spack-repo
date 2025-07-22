# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStreamer(RPackage):
	"""Enabling stream processing of large files

	Large data files can be difficult to work with in R, where data generally resides in memory. This package encourages a style of programming where data is 'streamed' from disk into R via a `producer' and through a series of `consumers' that, typically reduce the original data to a manageable size. The package provides useful Producer and Consumer stream components for operations such as data input, sampling, indexing, and transformation; see package?Streamer for details.
	"""
	
	bioc = "Streamer" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Streamer_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Streamer/Streamer_1.48.0.tar.gz"]

	version("1.54.0", tag="RELEASE_3_21")
	version("1.48.0", sha256="ab764572ff2c71f9a15554a3b575599e5adb4978dff15d0ea53d20e356ea3262")

	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
