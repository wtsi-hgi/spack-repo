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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SLqPCR_1.68.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SLqPCR/SLqPCR_1.68.0.tar.gz"]

	version("1.68.0", sha256="d7c950fe53bac9aa677475c81ef2a9b854078eb5c9ab14d99aefe01e2289cedc")

	depends_on("r@2.4:", type=("build", "run"))
