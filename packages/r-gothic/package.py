# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGothic(RPackage):
	"""Binomial test for Hi-C data analysis

	This is a Hi-C analysis package using a cumulative binomial test to detect interactions between distal genomic loci that have significantly more reads than expected by chance in Hi-C experiments. It takes mapped paired NGS reads as input and gives back the list of significant interactions for a given bin size in the genome.
	"""
	
	bioc = "GOTHiC" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GOTHiC_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GOTHiC/GOTHiC_1.38.0.tar.gz"]

	version("1.38.0", md5="4674978396dedfc730c8ad85662dac8c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors@0.9.38:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
