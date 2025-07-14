# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUcscrepeatmasker(RPackage):
	"""UCSC RepeatMasker AnnotationHub resource metadata

	Store UCSC RepeatMasker AnnotationHub resource metadata. Provide provenance and citation information for UCSC RepeatMasker AnnotationHub resources. Illustrate in a vignette how to access those resources.
	"""
	
	bioc = "UCSCRepeatMasker" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/UCSCRepeatMasker_3.15.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/UCSCRepeatMasker/UCSCRepeatMasker_3.15.2.tar.gz"]

	version("3.17.3", tag="RELEASE_3_21")
	version("3.15.2", sha256="677f01e2e21d1f94179bead18ec53af4615915a8cfad37c2e447b8b537822142")

	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))

