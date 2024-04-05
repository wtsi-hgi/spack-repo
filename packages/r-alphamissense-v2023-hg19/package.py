# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlphamissenseV2023Hg19(RPackage):
	"""AlphaMissense v2023 Pathogenicity Scores AnnotationHub Resource Metadata for hg19

	Store Google DeepMind AlphaMissense v2023 hg19 pathogenicity scores AnnotationHub Resource Metadata. Provide provenance and citation information for Google DeepMind AlphaMissense v2023 hg19 pathogenicity score AnnotationHub resources. Illustrate in a vignette how to access those resources.
	"""
	
	bioc = "AlphaMissense.v2023.hg19" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/AlphaMissense.v2023.hg19_3.18.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/AlphaMissense.v2023.hg19/AlphaMissense.v2023.hg19_3.18.2.tar.gz"]

	version("3.18.2", md5="e8784ad000be637321f432188a5a3f45", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/AlphaMissense.v2023.hg19_3.18.2.tar.gz")

	depends_on("r-genomicscores", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

