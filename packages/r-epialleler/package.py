# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpialleler(RPackage):
	"""Fast, Epiallele-Aware Methylation Caller and Reporter

	Epialleles are specific DNA methylation patterns that are mitotically and/or meiotically inherited. This package calls and reports cytosine methylation as well as frequencies of hypermethylated epialleles at the level of genomic regions or individual cytosines in next-generation sequencing data using binary alignment map (BAM) files as an input. Among other things, this package can also extract methylation patterns and assess allele specificity of methylation.
	"""
	
	homepage = "https://github.com/BBCG/epialleleR"
	bioc = "epialleleR"

	version("1.16.0", commit="91aa1ac3ac667045eb2d3d0812e5c6493e4e3118")
	version("1.10.0", commit="4b18f843425f39e961f575b9deeedec181d9d409")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rhtslib", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
	depends_on("curl", type=("build", "link", "run"))
