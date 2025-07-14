# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTvtb(RPackage):
	"""TVTB: The VCF Tool Box

	The package provides S4 classes and methods to filter, summarise and visualise genetic variation data stored in VCF files. In particular, the package extends the FilterRules class (S4Vectors package) to define news classes of filter rules applicable to the various slots of VCF objects. Functionalities are integrated and demonstrated in a Shiny web-application, the Shiny Variant Explorer (tSVE).
	"""
	
	homepage = "https://github.com/kevinrue/TVTB"
	bioc = "TVTB"

	version("1.34.0", commit="bbba86c2d6c502f1590bf28269aeee25152b4c13")
	version("1.28.0", commit="4bc60c26e2f9430650bd119e9ad56f510ab263bb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-annotationfilter", type=("build", "run"))
	depends_on("r-biocgenerics@0.25.1:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-ensemblvep", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-iranges@2.21.6:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-s4vectors@0.25.14:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-variantannotation@1.19.9:", type=("build", "run"))
