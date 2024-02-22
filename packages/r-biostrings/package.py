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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Biostrings_2.70.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Biostrings/Biostrings_2.70.2.tar.gz"]

	version("2.70.2", md5="05f7ef342dc92d017e36f61bfce48330")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocgenerics@0.37:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
