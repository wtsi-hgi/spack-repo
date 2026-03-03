# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcscan(RPackage):
	"""fcScan for detecting clusters of coordinates with user defined options

	This package is used to detect combination of genomic coordinates falling within a user defined window size along with user defined overlap between identified neighboring clusters. It can be used for genomic data where the clusters are built on a specific chromosome or specific strand. Clustering can be performed with a "greedy" option allowing thus the presence of additional sites within the allowed window size.
	"""
	
	bioc = "fcScan" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/fcScan_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/fcScan/fcScan_1.16.0.tar.gz"]

	version("1.16.0", md5="a23eab38b0106852ecca920f1f1db0bb")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
