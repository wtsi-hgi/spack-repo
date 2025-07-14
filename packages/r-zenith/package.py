# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZenith(RPackage):
	"""Gene set analysis following differential expression using linear (mixed) modeling with dream

	Zenith performs gene set analysis on the result of differential expression using linear (mixed) modeling with dream by considering the correlation between gene expression traits.  This package implements the camera method from the limma package proposed by Wu and Smyth (2012).  Zenith is a simple extension of camera to be compatible with linear mixed models implemented in variancePartition::dream().
	"""
	
	homepage = "https://DiseaseNeuroGenomics.github.io/zenith"
	bioc = "zenith" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/zenith_1.4.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/zenith/zenith_1.4.2.tar.gz"]

    version("1.10.0", tag="RELEASE_3_21")
	version("1.4.2", sha256="e4125d970e64108ee099b916fa4013b9f732ba4198d9ad838c50a27b93d9c373")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-variancepartition@1.26:", type=("build", "run"))
	depends_on("r-enrichmentbrowser@2.22:", type=("build", "run"))
	depends_on("r-gseabase@1.54:", type=("build", "run"))
	depends_on("r-msigdbr@7.5.1:", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
