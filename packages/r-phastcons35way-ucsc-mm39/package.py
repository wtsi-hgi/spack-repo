# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhastcons35wayUcscMm39(RPackage):
	"""UCSC phastCons mm39 conservation scores AnnotationHub Resource Metadata

	Store UCSC phastCons mm39 conservation scores AnnotationHub Resource Metadata. Provide provenance and citation information for UCSC phastCons mm39 conservation score AnnotationHub resources. Illustrate in a vignette how to access those resources.
	"""
	
	bioc = "phastCons35way.UCSC.mm39" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/phastCons35way.UCSC.mm39_3.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/phastCons35way.UCSC.mm39/phastCons35way.UCSC.mm39_3.16.0.tar.gz"]

	version("3.16.0", md5="83fc2a2265bc341b6a00064a1286b5bc", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/phastCons35way.UCSC.mm39_3.16.0.tar.gz")

	depends_on("r-genomicscores", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

