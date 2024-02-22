# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlqpcr(RPackage):
	"""Functions for analysis of real-time quantitative PCR data at SIRS-Lab GmbH

	Functions for analysis of real-time quantitative PCR data at SIRS-Lab GmbH
	"""
	
	bioc = "SLqPCR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SLqPCR_1.68.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SLqPCR/SLqPCR_1.68.0.tar.gz"]

	version("1.68.0", md5="72759fb6b62f3852f458e695318c0f6f")

	depends_on("r@2.4:", type=("build", "run"))
