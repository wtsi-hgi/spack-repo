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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/gmoviz_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/gmoviz/gmoviz_1.14.0.tar.gz"]

	version("1.20.0", tag="RELEASE_3_21")
	version("1.14.0", sha256="962fd20aa4e036f14594ed7dc1afdc305ee9ea53824e6d2ba12592fa1049191c")

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
