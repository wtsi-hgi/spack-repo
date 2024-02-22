# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScale4c(RPackage):
	"""Scale4C: an R/Bioconductor package for scale-space transformation of 4C-seq data

	Scale4C is an R/Bioconductor package for scale-space transformation and visualization of 4C-seq data. The scale-space transformation is a multi-scale visualization technique to transform a 2D signal (e.g. 4C-seq reads on a genomic interval of choice) into a tesselation in the scale space (2D, genomic position x scale factor) by applying different smoothing kernels (Gauss, with increasing sigma). This transformation allows for explorative analysis and comparisons of the data's structure with other samples.
	"""
	
	bioc = "Scale4C" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Scale4C_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Scale4C/Scale4C_1.24.0.tar.gz"]

	version("1.24.0", md5="7897932085759a05ad185eaec2afcd13")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-smoothie", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
