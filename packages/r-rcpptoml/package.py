# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcpptoml(RPackage):
	"""'Rcpp' Bindings to Parser for Tom's Obvious Markup Language.

	The configuration format defined by 'TOML' (which expands to "Tom's Obvious
	Markup Language") specifies an excellent format (described at
	<https://toml.io/en/>) suitable for both human editing as well as the
	common uses of a machine-readable format. This package uses 'Rcpp' to
	connect the 'cpptoml' parser written by Chase Geigle (in C++11) to R."""

	cran = "RcppTOML"

	license("JSON")

	version("0.2.2", md5="7ee285ee18fa1630c6595cb246a5a870")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
