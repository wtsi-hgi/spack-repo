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

	version("1.24.0", commit="d0675231a443b7fa51a10ecf932fa57e0ae92ce0")
	version("1.18.0", commit="a1ce82dcbe30d07ba7afe17531e34ca7057c6ae7")

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
