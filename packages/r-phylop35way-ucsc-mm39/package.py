# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylop35wayUcscMm39(RPackage):
	"""UCSC phyloP mm39 conservation scores AnnotationHub Resource Metadata

	Store UCSC phyloP mm39 conservation scores AnnotationHub Resource Metadata. Provide provenance and citation information for UCSC phyloP mm39 conservation score AnnotationHub resources. Illustrate in a vignette how to access those resources.
	"""
	
	bioc = "phyloP35way.UCSC.mm39" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/phyloP35way.UCSC.mm39_3.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/phyloP35way.UCSC.mm39/phyloP35way.UCSC.mm39_3.16.0.tar.gz"]

	version("3.16.0", md5="2c34eef5f20eace04efd47673cdf1062", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/phyloP35way.UCSC.mm39_3.16.0.tar.gz")

	depends_on("r-genomicscores", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

