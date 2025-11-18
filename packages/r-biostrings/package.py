# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiostrings(RPackage):
	"""Efficient manipulation of biological strings.

	Memory efficient string containers, string matching algorithms, and
	other utilities, for fast manipulation of large biological sequences or
	sets of sequences."""

	bioc = "Biostrings"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Biostrings_2.70.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Biostrings/Biostrings_2.70.3.tar.gz"]

	version("2.78.0", md5="b4ec1bf212646114ef729393f6ff3855", url="https://bioconductor.org/packages/3.22/bioc/src/contrib/Biostrings_2.78.0.tar.gz")
	version("2.70.3", md5="26220e6e7fe79bb5cc8b8b4ac9ec9d9d")
	version("2.70.2", md5="05f7ef342dc92d017e36f61bfce48330")
	version("2.68.0", commit="f28b7838fb8321a9956506b3d2f4af2740bca124")
	version("2.66.0", commit="3470ca7da798971e2c3a595d8dc8d0d86f14dc53")
	version("2.64.1", commit="ffe263e958463bd1edb5d5d9316cfd89905be53c")
	version("2.64.0", commit="c7ad3c7af607bc8fe4a5e1c37f09e6c9bf70b4f6")
	version("2.62.0", commit="53ed287e03d16fa523789af3131c60375ccf587f")
	version("2.58.0", commit="0ec1a5455d5e9eebd14b26228906bb04e2abb197")
	version("2.52.0", commit="b78fe7c1f3cdbbb7affb1ca7164fe5a1f8b868f5")
	version("2.50.2", commit="025e734641a93f6c5d44243297cb4264ea0e34a2")
	version("2.48.0", commit="aa3599a7d259d658014d087b86d71ab1deb5f12b")
	version("2.46.0", commit="3bf6978c155498b50607d1bb471d1687d185a0fa")
	version("2.44.2", commit="e4a2b320fb21c5cab3ece7b3c6fecaedfb1e5200")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocgenerics@0.37:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
