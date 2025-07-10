# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylseekr(RPackage):
	"""Segmentation of Bis-seq data

	This is a package for the discovery of regulatory regions from Bis-seq data
	"""
	
	bioc = "MethylSeekR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MethylSeekR_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MethylSeekR/MethylSeekR_1.42.0.tar.gz"]

	version("1.42.0", sha256="eeb5fe4f96fecae75a0197044c8ee1ea493efd0ab68dfa15236971753e56517f")

	depends_on("r-rtracklayer@1.16.3:", type=("build", "run"))
	depends_on("r-mhsmm@0.4.4:", type=("build", "run"))
	depends_on("r-iranges@1.16.3:", type=("build", "run"))
	depends_on("r-bsgenome@1.26.1:", type=("build", "run"))
	depends_on("r-genomicranges@1.10.5:", type=("build", "run"))
	depends_on("r-geneplotter@1.34:", type=("build", "run"))
