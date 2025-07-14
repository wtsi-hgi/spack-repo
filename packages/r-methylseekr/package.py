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

	version("1.48.0", commit="6e4e7fe7584f8775064b5c80d1afd938ed8f460c")
	version("1.42.0", commit="40b73b2d40378fc5e1111e348f24092457d4e1bc")

	depends_on("r-rtracklayer@1.16.3:", type=("build", "run"))
	depends_on("r-mhsmm@0.4.4:", type=("build", "run"))
	depends_on("r-iranges@1.16.3:", type=("build", "run"))
	depends_on("r-bsgenome@1.26.1:", type=("build", "run"))
	depends_on("r-genomicranges@1.10.5:", type=("build", "run"))
	depends_on("r-geneplotter@1.34:", type=("build", "run"))
