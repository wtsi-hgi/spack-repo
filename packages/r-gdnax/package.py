# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdnax(RPackage):
	"""Diagnostics for assessing genomic DNA contamination in RNA-seq data

	Provides diagnostics for assessing genomic DNA contamination in RNA-seq data, as well as plots representing these diagnostics. Moreover, the package can be used to get an insight into the strand library protocol used and, in case of strand-specific libraries, the strandedness of the data. Furthermore, it provides functionality to filter out reads of potential gDNA origin.
	"""
	
	homepage = "https://github.com/functionalgenomics/gDNAx"
	bioc = "gDNAx" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/gDNAx_1.0.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/gDNAx/gDNAx_1.0.2.tar.gz"]

	version("1.0.2", md5="e8937acc1de3e0e87a81c446a928d98f")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicfiles", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
