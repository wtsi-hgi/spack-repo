# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSomnibus(RPackage):
	"""Smooth modeling of bisulfite sequencing

	This package aims to analyse count-based methylation data on predefined genomic regions, such as those obtained by targeted sequencing, and thus to identify differentially methylated regions (DMRs) that are associated with phenotypes or traits. The method is built a rich flexible model that allows for the effects, on the methylation levels, of multiple covariates to vary smoothly along genomic regions. At the same time, this method also allows for sequencing errors and can adjust for variability in cell type mixture.
	"""
	
	homepage = "https://github.com/kaiqiong/SOMNiBUS"
	bioc = "SOMNiBUS" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SOMNiBUS_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SOMNiBUS/SOMNiBUS_1.10.0.tar.gz"]

	version("1.10.0", md5="0865c015122f915127302bf751a10812")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-annotatr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-bsseq", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
