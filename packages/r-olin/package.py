# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROlin(RPackage):
	"""Optimized local intensity-dependent normalisation of two-color microarrays

	Functions for normalisation of two-color microarrays by optimised local regression and for detection of artefacts in microarray data
	"""
	
	homepage = "http://olin.sysbiolab.eu"
	bioc = "OLIN" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/OLIN_1.80.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/OLIN/OLIN_1.80.0.tar.gz"]

	version("1.80.0", sha256="d983961e34feb154c35b8bdebe91d6339e7d90bb500cc32ceed38c88ca5052f3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
