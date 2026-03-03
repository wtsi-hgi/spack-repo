# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmicade4(RPackage):
	"""Multiple co-inertia analysis of omics datasets

	This package performes multiple co-inertia analysis of omics datasets.
	"""
	
	bioc = "omicade4" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/omicade4_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/omicade4/omicade4_1.42.0.tar.gz"]

	version("1.42.0", md5="ed6de2f603d54a9ad262ff62784818a2", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/omicade4_1.42.0.tar.gz")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-made4", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
