# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqHotspot(RPackage):
	"""Targeted sequencing panel design based on mutation hotspots

	seq.hotSPOT provides a resource for designing effective sequencing panels to help improve mutation capture efficacy for ultradeep sequencing projects. Using SNV datasets, this package designs custom panels for any tissue of interest and identify the genomic regions likely to contain the most mutations. Establishing efficient targeted sequencing panels can allow researchers to study mutation burden in tissues at high depth without the economic burden of whole-exome or whole-genome sequencing. This tool was developed to make high-depth sequencing panels to study low-frequency clonal mutations in clinically normal and cancerous tissues.
	"""
	
	homepage = "https://github.com/sydney-grant/seq.hotSPOT"
	bioc = "seq.hotSPOT" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/seq.hotSPOT_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/seq.hotSPOT/seq.hotSPOT_1.2.0.tar.gz"]

	version("1.2.0", md5="37e04dc7e1bb05af58c50cb7701388c7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
