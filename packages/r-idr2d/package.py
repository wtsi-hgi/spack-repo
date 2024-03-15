# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdr2d(RPackage):
	"""Irreproducible Discovery Rate for Genomic Interactions Data

	A tool to measure reproducibility between genomic experiments that produce two-dimensional peaks (interactions between peaks), such as ChIA-PET, HiChIP, and HiC. idr2d is an extension of the original idr package, which is intended for (one-dimensional) ChIP-seq peaks.
	"""
	
	homepage = "https://idr2d.mit.edu"
	bioc = "idr2d" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/idr2d_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/idr2d/idr2d_1.16.0.tar.gz"]

	version("1.16.0", md5="6662b2b18dc8c6029ad40099c5fcd6a7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-futile-logger@1.4.3:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.14:", type=("build", "run"))
	depends_on("r-genomicranges@1.30:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-idr@1.2:", type=("build", "run"))
	depends_on("r-iranges@2.18:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-reticulate@1.13:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("python@3.5.0:", type=("build", "link", "run"))
