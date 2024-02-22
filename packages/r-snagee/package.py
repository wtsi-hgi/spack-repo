# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnagee(RPackage):
	"""Signal-to-Noise applied to Gene Expression Experiments

	Signal-to-Noise applied to Gene Expression Experiments. Signal-to-noise ratios can be used as a proxy for quality of gene expression studies and samples. The SNRs can be calculated on any gene expression data set as long as gene IDs are available, no access to the raw data files is necessary. This allows to flag problematic studies and samples in any public data set.
	"""
	
	homepage = "http://bioconductor.org/"
	bioc = "SNAGEE" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SNAGEE_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SNAGEE/SNAGEE_1.42.0.tar.gz"]

	version("1.42.0", md5="faadcab23b170f71a29ac7fd67b2a5d8")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-snageedata", type=("build", "run"))
