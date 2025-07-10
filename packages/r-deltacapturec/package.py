# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeltacapturec(RPackage):
	"""This Package Discovers Meso-scale Chromatin Remodeling from 3C Data

	This package discovers meso-scale chromatin remodelling from 3C data.  3C data is local in nature.  It givens interaction counts between restriction enzyme digestion fragments and a preferred 'viewpoint' region.  By binning this data and using permutation testing, this package can test whether there are statistically significant changes in the interaction counts between the data from two cell types or two treatments.
	"""
	
	bioc = "deltaCaptureC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/deltaCaptureC_1.16.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/deltaCaptureC/deltaCaptureC_1.16.1.tar.gz"]

	version("1.16.1", sha256="2e40fd19dddc7a2fff077b9a5ad917d1726604a3b84aa7e51c88f9f4a645bc53")
	version("1.16.0", md5="e70cf57b6d22164dd5712a3441b0a788")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
