# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPreprocesscore(RPackage):
	"""A collection of pre-processing functions.

	A library of core preprocessing routines."""

	bioc = "preprocessCore"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/preprocessCore_1.64.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/preprocessCore/preprocessCore_1.64.0.tar.gz"]

	version("1.64.0", md5="2116c6363074b59becdaf7a1e88caf91")

