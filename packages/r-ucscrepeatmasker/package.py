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

	version("3.17.3", commit="a64273762811970917fc3a47499271c96feede0e")
	version("3.15.2", commit="e06066a9240755777c81796752bda1947215055f")

	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))

