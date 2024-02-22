# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfpred(RPackage):
	"""Assign rfPred functional prediction scores to a missense variants list

	Based on external numerous data files where rfPred scores are pre-calculated on all genomic positions of the human exome, the package gives rfPred scores to missense variants identified by the chromosome, the position (hg19 version), the referent and alternative nucleotids and the uniprot identifier of the protein. Note that for using the package, the user has to download the TabixFile and index (approximately 3.3 Go).
	"""
	
	bioc = "rfPred" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/rfPred_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/rfPred/rfPred_1.40.0.tar.gz"]

	version("1.40.0", md5="125e88d593749d17979dfd08a67ea330")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
