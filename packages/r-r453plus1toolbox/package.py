# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR453plus1toolbox(RPackage):
	"""A package for importing and analyzing data from Roche's Genome Sequencer System

	The R453Plus1 Toolbox comprises useful functions for the analysis of data generated by Roche's 454 sequencing platform. It adds functions for quality assurance as well as for annotation and visualization of detected variants, complementing the software tools shipped by Roche with their product. Further, a pipeline for the detection of structural variants is provided.
	"""
	
	bioc = "R453Plus1Toolbox" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/R453Plus1Toolbox_1.52.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/R453Plus1Toolbox/R453Plus1Toolbox_1.52.0.tar.gz"]

	version("1.52.0", md5="2d7ad69c3b68b4a635129d296599c210")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-variantannotation@1.25.11:", type=("build", "run"))
	depends_on("r-biostrings@2.47.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-r2html", type=("build", "run"))
	depends_on("r-teachingdemos", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors@0.17.25:", type=("build", "run"))
	depends_on("r-iranges@2.13.12:", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-genomicranges@1.31.8:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-bsgenome@1.47.3:", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-shortread@1.37.1:", type=("build", "run"))
