# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPuma(RPackage):
	"""Propagating Uncertainty in Microarray Analysis(including Affymetrix tranditional 3' arrays and exon arrays and Human Transcriptome Array 2.0)

	Most analyses of Affymetrix GeneChip data (including tranditional 3' arrays and exon arrays and Human Transcriptome Array 2.0) are based on point estimates of expression levels and ignore the uncertainty of such estimates. By propagating uncertainty to downstream analyses we can improve results from microarray analyses. For the first time, the puma package makes a suite of uncertainty propagation methods available to a general audience. In additon to calculte gene expression from Affymetrix 3' arrays, puma also provides methods to process exon arrays and produces gene and isoform expression for alternative splicing study. puma also offers improvements in terms of scope and speed of execution over previously available uncertainty propagation methods. Included are summarisation, differential expression detection, clustering and PCA methods, together with useful plotting functions.
	"""
	
	homepage = "http://umber.sbs.man.ac.uk/resources/puma"
	bioc = "puma" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/puma_3.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/puma/puma_3.44.0.tar.gz"]

	version("3.44.0", md5="ed1d90c9c9b7751611b0f32edf0a1ffb")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-oligo@1.32:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-oligoclasses", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-affy@1.46:", type=("build", "run"))
	depends_on("r-affyio", type=("build", "run"))
