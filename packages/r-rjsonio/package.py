# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjsonio(RPackage):
	"""Serialize R Objects to JSON, JavaScript Object Notation.

	This is a package that allows conversion to and from data in Javascript
	object notation (JSON) format. This allows R objects to be inserted into
	Javascript/ECMAScript/ActionScript code and allows R programmers to read
	and convert JSON content to R objects. This is an alternative to rjson
	package. Originally, that was too slow for converting large R objects to
	JSON and was not extensible. rjson's performance is now similar to this
	package, and perhaps slightly faster in some cases. This package uses
	methods and is readily extensible by defining methods for different
	classes, vectorized operations, and C code and callbacks to R functions for
	deserializing JSON objects to R. The two packages intentionally share the
	same basic interface. This package (RJSONIO) has many additional options to
	allow customizing the generation and processing of JSON content. This
	package uses libjson rather than implementing yet another JSON parser. The
	aim is to support other general projects by building on their work,
	providing feedback and benefit from their ongoing development."""

	cran = "RJSONIO"

	version("1.3-1.9", md5="d42747c9c3be446a3aefa2b9fa28023c")

