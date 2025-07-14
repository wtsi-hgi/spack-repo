# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModa(RPackage):
	"""MODA: MOdule Differential Analysis for weighted gene co-expression network

	MODA can be used to estimate and construct condition-specific gene co-expression networks, and identify differentially expressed subnetworks as conserved or condition specific modules which are potentially associated with relevant biological processes.
	"""
	
	bioc = "MODA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MODA_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MODA/MODA_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="824b7dac0b2340a327ca7ac80fc9f2312fac24234c4b5546cd6373f31c35b5ab")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-amountain", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
