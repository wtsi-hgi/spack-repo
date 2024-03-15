# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdpack(RPackage):
	"""Update and Manipulate Rd Documentation Objects.

	Functions for manipulation of R documentation objects, including functions
	reprompt() and ereprompt() for updating 'Rd' documentation for functions,
	methods and classes; 'Rd' macros for citations and import of references
	from 'bibtex' files for use in 'Rd' files and 'roxygen2' comments; 'Rd'
	macros for evaluating and inserting snippets of 'R' code and the results of
	its evaluation or creating graphics on the fly; and many functions for
	manipulation of references and Rd files."""

	cran = "Rdpack"

	version("2.6", md5="212a5f9ba8330ae43f266d3d598fbc3a")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-rbibutils@1.3:", type=("build", "run"))
