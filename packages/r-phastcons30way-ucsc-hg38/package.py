# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhastcons30wayUcscHg38(RPackage):
	"""phastCons30way.UCSC.hg38 AnnotationHub Resource Metadata

	Store phastCons30way.UCSC.hg38 AnnotationHub Resource Metadata.
	"""
	
	bioc = "phastCons30way.UCSC.hg38" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/phastCons30way.UCSC.hg38_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/phastCons30way.UCSC.hg38/phastCons30way.UCSC.hg38_3.13.0.tar.gz"]

	version("3.13.0", md5="754faee8463bc494c502540cb8f6ea8d", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/phastCons30way.UCSC.hg38_3.13.0.tar.gz")

	depends_on("r-genomicscores", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

