# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegutools(RPackage):
	"""regutools: an R package for data extraction from RegulonDB

	RegulonDB has collected, harmonized and centralized data from hundreds of experiments for nearly two decades and is considered a point of reference for transcriptional regulation in Escherichia coli K12. Here, we present the regutools R package to facilitate programmatic access to RegulonDB data in computational biology. regutools provides researchers with the possibility of writing reproducible workflows with automated queries to RegulonDB. The regutools package serves as a bridge between RegulonDB data and the Bioconductor ecosystem by reusing the data structures and statistical methods powered by other Bioconductor packages. We demonstrate the integration of regutools with Bioconductor by analyzing transcription factor DNA binding sites and transcriptional regulatory networks from RegulonDB. We anticipate that regutools will serve as a useful building block in our progress to further our understanding of gene regulatory networks.
	"""
	
	homepage = "https://github.com/ComunidadBioInfo/regutools"
	bioc = "regutools" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/regutools_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/regutools/regutools_1.14.0.tar.gz"]

	version("1.14.0", md5="f8b22dfa98af4304de7be1654159626a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rcy3", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
