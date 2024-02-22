# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffycomp(RPackage):
	"""Graphics Toolbox for Assessment of Affymetrix Expression Measures.

	The package contains functions that can be used to compare expression
	measures for Affymetrix Oligonucleotide Arrays."""

	bioc = "affycomp"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/affycomp_1.78.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/affycomp/affycomp_1.78.0.tar.gz"]

	version("1.78.0", md5="f80b53dc57dcb88730eda3c0506b9df1")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-biobase@2.3.3:", type=("build", "run"))
