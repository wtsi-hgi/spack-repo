# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnotationhubdata(RPackage):
	"""Transform public data resources into Bioconductor Data Structures

	These recipes convert a wide variety and a growing number of public bioinformatic data sets into easily-used standard Bioconductor data structures.
	"""
	
	bioc = "AnnotationHubData" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/AnnotationHubData_1.32.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/AnnotationHubData/AnnotationHubData_1.32.1.tar.gz"]

    version("1.38.0", tag="RELEASE_3_21")
	version("1.32.1", sha256="b59ea2632ce440ef7a3ae7ac1c219b5f10a897b0d2397973147253319cb4a227")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-s4vectors@0.7.21:", type=("build", "run"))
	depends_on("r-iranges@2.3.23:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-annotationhub@2.15.15:", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-biocviews", type=("build", "run"))
	depends_on("r-bioccheck", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-genomeinfodb@1.15.4:", type=("build", "run"))
	depends_on("r-organismdbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-annotationforge", type=("build", "run"))
	depends_on("r-futile-logger@1.3:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
