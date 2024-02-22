# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomeinfodb(RPackage):
	"""Utilities for manipulating chromosome names, including modifying them to
	follow a particular naming style.

	Contains data and functions that define and allow translation between
	different chromosome sequence naming conventions (e.g., "chr1" versus
	"1"), including a function that attempts to place sequence names in
	their natural, rather than lexicographic, order."""

	bioc = "GenomeInfoDb"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GenomeInfoDb_1.38.6.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GenomeInfoDb/GenomeInfoDb_1.38.6.tar.gz"]

	version("1.38.6", md5="b739753a88d5a331b38744b1ad14f416")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocgenerics@0.37:", type=("build", "run"))
	depends_on("r-s4vectors@0.25.12:", type=("build", "run"))
	depends_on("r-iranges@2.13.12:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-genomeinfodbdata", type=("build", "run"))
