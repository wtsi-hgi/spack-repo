# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaseqpower(RPackage):
	"""Sample size for RNAseq studies

	RNA-seq, sample size
	"""
	
	bioc = "RNASeqPower" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RNASeqPower_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RNASeqPower/RNASeqPower_1.42.0.tar.gz"]

	version("1.42.0", md5="38da142eb3ee64f2e7684ead27e4520f")

