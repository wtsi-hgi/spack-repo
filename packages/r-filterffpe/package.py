# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFilterffpe(RPackage):
	"""FFPE Artificial Chimeric Read Filter for NGS data

	This package finds and filters artificial chimeric reads specifically generated in next-generation sequencing (NGS) process of formalin-fixed paraffin-embedded (FFPE) tissues. These artificial chimeric reads can lead to a large number of false positive structural variation (SV) calls. The required input is an indexed BAM file of a FFPE sample.
	"""
	
	bioc = "FilterFFPE" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/FilterFFPE_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/FilterFFPE/FilterFFPE_1.12.0.tar.gz"]

	version("1.12.0", md5="e2aabe533af9d2779d1ffc2f76017ecd")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
