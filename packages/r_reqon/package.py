# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReqon(RPackage):
	"""Recalibrating Quality Of Nucleotides

	Algorithm for recalibrating the base quality scores for aligned sequencing data in BAM format.
	"""
	
	bioc = "ReQON" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ReQON_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ReQON/ReQON_1.48.0.tar.gz"]

	version("1.48.0", md5="3940db44a4b48a5b04d87c9466df72c3")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-seqbias", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("openjdk@1.6:", type=("build", "link", "run"))
