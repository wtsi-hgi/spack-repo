# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastseg(RPackage):
	"""fastseg - a fast segmentation algorithm

	fastseg implements a very fast and efficient segmentation algorithm. It has similar functionality as DNACopy (Olshen and Venkatraman 2004), but is considerably faster and more flexible. fastseg can segment data from DNA microarrays and data from next generation sequencing for example to detect copy number segments. Further it can segment data from RNA microarrays like tiling arrays to identify transcripts. Most generally, it can segment data given as a matrix or as a vector. Various data formats can be used as input to fastseg like expression set objects for microarrays or GRanges for sequencing data. The segmentation criterion of fastseg is based on a statistical test in a Bayesian framework, namely the cyber t-test (Baldi 2001). The speed-up arises from the facts, that sampling is not necessary in for fastseg and that a dynamic programming approach is used for calculation of the segments' first and higher order moments.
	"""
	
	homepage = "http://www.bioinf.jku.at/software/fastseg/index.html"
	bioc = "fastseg" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/fastseg_1.48.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/fastseg/fastseg_1.48.0.tar.gz"]

	version("1.48.0", md5="ca8ead071a9b881b19dea7b71e0e73b4")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
