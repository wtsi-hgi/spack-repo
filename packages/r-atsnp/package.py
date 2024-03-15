# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtsnp(RPackage):
	"""Affinity test for identifying regulatory SNPs

	atSNP performs affinity tests of motif matches with the SNP or the reference genomes and SNP-led changes in motif matches.
	"""
	
	homepage = "https://github.com/sunyoungshin/atSNP"
	bioc = "atSNP" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/atSNP_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/atSNP/atSNP_1.18.0.tar.gz"]

	version("1.18.0", md5="e7de15cd417026f8449b14841ff89bd2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-motifstack", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
