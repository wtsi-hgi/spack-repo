# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtf(RPackage):
	"""Read and Write Column Text Format (CTF)

	
    Column Text Format (CTF) is a new tabular data format designed for simplicity and performance.
    CTF is the simplest column store you can imagine: plain text files for each column in a table, and a metadata file.
    The underlying plain text means the data is human readable and familiar to programmers, unlike specialized binary formats.
    CTF is faster than row oriented formats like CSV when loading a subset of the columns in a table.
    This package provides functions to read and write CTF data from R.
	"""
	
	homepage = "https://github.com/julianofhernandez/ctf"
	cran = "ctf" 

	version("0.1.0", md5="27362df30bdc5fa326844ebb07c677a4")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-iotools", type=("build", "run"))
