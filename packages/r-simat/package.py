# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimat(RPackage):
	"""GC-SIM-MS data processing and alaysis tool

	This package provides a pipeline for analysis of GC-MS data acquired in selected ion monitoring (SIM) mode. The tool also provides a guidance in choosing appropriate fragments for the targets of interest by using an optimization algorithm. This is done by considering overlapping peaks from a provided library by the user.
	"""
	
	homepage = "http://omics.georgetown.edu/SIMAT.html"
	bioc = "SIMAT" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SIMAT_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SIMAT/SIMAT_1.34.0.tar.gz"]

	version("1.34.0", sha256="3d21223855349c651f2524ae3115ca7d35149a2a120fce0358d98dfe59f326d9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.11.3:", type=("build", "run"))
	depends_on("r-mzr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
