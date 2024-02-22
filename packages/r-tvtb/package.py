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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/TVTB_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/TVTB/TVTB_1.28.0.tar.gz"]

	version("1.28.0", md5="64da00f3c21bf3f9a82dc32e451395a1")

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
