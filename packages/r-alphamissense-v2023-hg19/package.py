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

	version("3.18.2", commit="f8b2919c870c9b59e236f871e38a8606f8c0789a")
	version("3.18.2", commit="f8b2919c870c9b59e236f871e38a8606f8c0789a")

	depends_on("r-genomicscores", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

