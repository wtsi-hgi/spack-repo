# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenome(RPackage):
	"""Software infrastructure for efficient representation of full genomes and
	   their SNPs.

	Infrastructure shared by all the Biostrings-based genome data packages."""

	bioc = "BSgenome"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BSgenome_1.70.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BSgenome/BSgenome_1.70.2.tar.gz"]

	version("1.70.2", md5="6a77e5c7815ff39c5942a4d34c05a105")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-biocgenerics@0.13.8:", type=("build", "run"))
	depends_on("r-s4vectors@0.17.28:", type=("build", "run"))
	depends_on("r-iranges@2.13.16:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.25.6:", type=("build", "run"))
	depends_on("r-genomicranges@1.31.10:", type=("build", "run"))
	depends_on("r-biostrings@2.47.6:", type=("build", "run"))
	depends_on("r-biocio", type=("build", "run"))
	depends_on("r-rtracklayer@1.39.7:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
