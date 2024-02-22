# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWk(RPackage):
	"""Lightweight Well-Known Geometry Parsing.

	Provides a minimal R and C++ API for parsing well-known binary and
	well-known text representation of geometries to and from R-native formats.
	Well-known binary is compact and fast to parse; well-known text is
	human-readable and is useful for writing tests. These formats are only
	useful in R if the information they contain can be accessed in R, for which
	high-performance functions are provided here."""

	cran = "wk"

	version("0.9.1", md5="347bbbd47d5c419d0238f034a942ec22")

	depends_on("r@2.10:", type=("build", "run"))
