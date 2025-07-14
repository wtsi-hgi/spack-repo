# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVulcan(RPackage):
	"""VirtUaL ChIP-Seq data Analysis using Networks

	Vulcan (VirtUaL ChIP-Seq Analysis through Networks) is a package that interrogates gene regulatory networks to infer cofactors significantly enriched in a differential binding signature coming from ChIP-Seq data. In order to do so, our package combines strategies from different BioConductor packages: DESeq for data normalization, ChIPpeakAnno and DiffBind for annotation and definition of ChIP-Seq genomic peaks, csaw to define optimal peak width and viper for applying a regulatory network over a differential binding signature.
	"""
	
	bioc = "vulcan" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/vulcan_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/vulcan/vulcan_1.24.0.tar.gz"]

    version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="bfd2125e94f0e99590c572ab503d409c536180fd1ffc662bb1f9f66e2a4b4c7f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-chippeakanno", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-viper", type=("build", "run"))
	depends_on("r-diffbind", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
	depends_on("r-csaw", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
