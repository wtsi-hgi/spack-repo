# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPurecn(RPackage):
	"""Copy number calling and SNV classification using targeted short read sequencing

	This package estimates tumor purity, copy number, and loss of heterozygosity (LOH), and classifies single nucleotide variants (SNVs) by somatic status and clonality. PureCN is designed for targeted short read sequencing data, integrates well with standard somatic variant detection and copy number pipelines, and has support for tumor samples without matching normal samples.
	"""
	
	homepage = "https://github.com/lima1/PureCN"
	bioc = "PureCN" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PureCN_2.8.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PureCN/PureCN_2.8.1.tar.gz"]

	version("2.14.1", tag="RELEASE_3_21")
	version("2.8.1", sha256="f2ac2ee30b8da345f3170f964ef79c61b19ca85948fc6bdcb374d32e64702142")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-variantannotation@1.14.1:", type=("build", "run"))
	depends_on("r-genomicranges@1.20.3:", type=("build", "run"))
	depends_on("r-iranges@2.2.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
