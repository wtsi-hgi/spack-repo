# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJsonlite(RPackage):
	"""A Simple and Robust JSON Parser and Generator for R.

	A fast JSON parser and generator optimized for statistical data and the
	web. Started out as a fork of 'RJSONIO', but has been completely rewritten
	in recent versions. The package offers flexible, robust, high performance
	tools for working with JSON in R and is particularly powerful for building
	pipelines and interacting with a web API. The implementation is based on
	the mapping described in the vignette (Ooms, 2014). In addition to
	converting JSON data from/to R objects, 'jsonlite' contains functions to
	stream, validate, and prettify JSON data. The unit tests included with the
	package verify that all edge cases are encoded and decoded consistently for
	use with dynamic data in systems and applications."""

	cran = "jsonlite"

	version("1.8.8", md5="d1ec8467abf43d41aabeec24d5a9096a")

