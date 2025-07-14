# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqgate(RPackage):
	"""Filtering of Lowly Expressed Features

	Filtering of lowly expressed features (e.g. genes) is a common step before performing statistical analysis, but an arbitrary threshold is generally chosen. SeqGate implements a method that rationalize this step by the analysis of the distibution of counts in replicate samples. The gate is the threshold above which sequenced features can be considered as confidently quantified.
	"""
	
	bioc = "SeqGate" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SeqGate_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SeqGate/SeqGate_1.12.0.tar.gz"]

    version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="63c32370dcd8f96edef04104858dffe3714f30b4bae38687962fe01834df7e5e")

	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
