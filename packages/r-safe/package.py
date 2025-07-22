# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSafe(RPackage):
	"""Significance Analysis of Function and Expression

	SAFE is a resampling-based method for testing functional categories in gene expression experiments. SAFE can be applied to 2-sample and multi-class comparisons, or simple linear regressions. Other experimental designs can also be accommodated through user-defined functions.
	"""
	
	bioc = "safe" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/safe_3.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/safe/safe_3.42.0.tar.gz"]

    version("3.48.0", tag="RELEASE_3_21")
	version("3.42.0", sha256="58506ffefd54b8711081e7ef3ebf13132384b618a16daa3a58f8c15a93e81af4")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
