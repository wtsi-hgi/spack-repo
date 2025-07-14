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

	version("1.54.0", commit="6736770163ea762572222b45dcc01e983476e509")
	version("1.48.0", commit="3e1a31458b3a42d47feb2ffc6bbdf8d8fae89b82")

	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
