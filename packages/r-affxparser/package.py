# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffxparser(RPackage):
	"""Affymetrix File Parsing SDK.

	Package for parsing Affymetrix files (CDF, CEL, CHP, BPMAP, BAR). It
	provides methods for fast and memory efficient parsing of Affymetrix
	files using the Affymetrix' Fusion SDK. Both ASCII- and binary-based
	files are supported. Currently, there are methods for reading chip
	definition file (CDF) and a cell intensity file (CEL). These files can
	be read either in full or in part. For example, probe signals from a few
	probesets can be extracted very quickly from a set of CEL files into a
	convenient list structure."""

	bioc = "affxparser"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/affxparser_1.74.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/affxparser/affxparser_1.74.0.tar.gz"]

	version("1.74.0", md5="2b6b9373d749a0ccbf930f834df90b92")

	depends_on("r@2.14:", type=("build", "run"))
