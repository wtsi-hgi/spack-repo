# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScreencounter(RPackage):
	"""Counting Reads in High-Throughput Sequencing Screens

	Provides functions for counting reads from high-throughput sequencing screen data (e.g., CRISPR, shRNA) to quantify barcode abundance. Currently supports single barcodes in single- or paired-end data, and combinatorial barcodes in paired-end data.
	"""

	homepage = "https://github.com/crisprVerse/screenCounter"
	bioc = "screenCounter"
	urls = [
	    "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/screenCounter_1.2.0.tar.gz",
	    "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/screenCounter/screenCounter_1.2.0.tar.gz",
	]

	version("1.8.0", tag="RELEASE_3_21")
	version("1.2.0", sha256="a9995014d30f1a8856794a65b2f34a0db6a662e29f11947058359cecce0c68fa")

	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("zlib-api", type=("build", "run", "link"))
