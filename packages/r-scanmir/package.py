# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScanmir(RPackage):
	"""scanMiR

	A set of tools for working with miRNA affinity models (KdModels), efficiently scanning for miRNA binding sites, and predicting target repression. It supports scanning using miRNA seeds, full miRNA sequences (enabling 3' alignment) and KdModels, and includes the prediction of slicing and TDMD sites. Finally, it includes utility and plotting functions (e.g. for the visual representation of miRNA-target alignment).
	"""
	
	bioc = "scanMiR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scanMiR_1.8.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scanMiR/scanMiR_1.8.2.tar.gz"]

    version("1.14.0", tag="RELEASE_3_21")
	version("1.8.2", sha256="8bdedaff1b02a44d93076c7543e74c42c6b74982714fcf56372f0cb342e39f81")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-seqlogo", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggseqlogo", type=("build", "link", "run"))
