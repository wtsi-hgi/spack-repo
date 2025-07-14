# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCasper(RPackage):
	"""Characterization of Alternative Splicing based on Paired-End Reads

	Infer alternative splicing from paired-end RNA-seq data. The model is based on counting paths across exons, rather than pairwise exon connections, and estimates the fragment size and start distributions non-parametrically, which improves estimation precision.
	"""
	
	bioc = "casper"

	version("2.42.0", commit="8d20bffb2ab7e7826fb87a6a6a8881abedd39c93")
	version("2.36.0", commit="10bb58568406f6149e4dc043ee04b9c23a335d5e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocgenerics@0.31.6:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ebarrays", type=("build", "run"))
	depends_on("r-gaga", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
