# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnvfilter(RPackage):
	"""Identifies false positives of CNV calling tools by using SNV calls

	CNVfilteR identifies those CNVs that can be discarded by using the single nucleotide variant (SNV) calls that are usually obtained in common NGS pipelines.
	"""
	
	homepage = "https://github.com/jpuntomarcos/CNVfilteR"
	bioc = "CNVfilteR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CNVfilteR_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CNVfilteR/CNVfilteR_1.16.0.tar.gz"]

    version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="6aa5f05b81106265824094f7446baddd4365268a818b870929c7f08068f1fabd")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-regioner", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-karyoploter", type=("build", "run"))
	depends_on("r-copynumberplots", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
