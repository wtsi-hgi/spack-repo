# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaddV16Hg19(RPackage):
	"""CADD v1.6 Pathogenicity Scores AnnotationHub Resource Metadata for hg19

	Store University of Washington CADD v1.6 hg19 pathogenicity scores AnnotationHub Resource Metadata. Provide provenance and citation information for University of Washington CADD v1.6 hg19 pathogenicity score AnnotationHub resources. Illustrate in a vignette how to access those resources.
	"""
	
	bioc = "cadd.v1.6.hg19" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/cadd.v1.6.hg19_3.18.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/cadd.v1.6.hg19/cadd.v1.6.hg19_3.18.1.tar.gz"]

	version("3.18.1", md5="10cc50d17dbca89406a2290f37d5203c", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/cadd.v1.6.hg19_3.18.1.tar.gz")

	depends_on("r-genomicscores", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

