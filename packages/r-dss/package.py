# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDss(RPackage):
	"""Dispersion shrinkage for sequencing data.

	DSS is an R library performing differntial analysis for count-based
	sequencing data. It detectes differentially expressed genes (DEGs) from
	RNA-seq, and differentially methylated loci or regions (DML/DMRs) from
	bisulfite sequencing (BS-seq). The core of DSS is a new dispersion
	shrinkage method for estimating the dispersion parameter from Gamma-Poisson
	or Beta-Binomial distributions."""

	bioc = "DSS"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DSS_2.50.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DSS/DSS_2.50.1.tar.gz"]

	version("2.50.1", md5="96713d3519e0dcf2f1331b7e9a8dbb95")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-bsseq", type=("build", "run"))
