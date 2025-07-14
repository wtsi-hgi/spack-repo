# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmoviz(RPackage):
	"""Seamless visualization of complex genomic variations in GMOs and edited cell lines

	Genetically modified organisms (GMOs) and cell lines are widely used models in all kinds of biological research. As part of characterising these models, DNA sequencing technology and bioinformatics analyses are used systematically to study their genomes. Therefore, large volumes of data are generated and various algorithms are applied to analyse this data, which introduces a challenge on representing all findings in an informative and concise manner. `gmoviz` provides users with an easy way to visualise and facilitate the explanation of complex genomic editing events on a larger, biologically-relevant scale.
	"""
	
	bioc = "gmoviz"

	version("1.20.0", commit="cc16d9e8877921f2bcc0376d995e95410f5fc963")
	version("1.14.0", commit="1bc517f1599b11651ff96d4764e80715e1fbfca2")

	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
