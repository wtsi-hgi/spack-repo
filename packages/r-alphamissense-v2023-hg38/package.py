# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlphamissenseV2023Hg38(RPackage):
	"""AlphaMissense v2023 Pathogenicity Scores AnnotationHub Resource Metadata for hg38

	Store Google DeepMind AlphaMissense v2023 hg38 pathogenicity scores AnnotationHub Resource Metadata. Provide provenance and citation information for Google DeepMind AlphaMissense v2023 hg38 pathogenicity score AnnotationHub resources. Illustrate in a vignette how to access those resources.
	"""
	
	bioc = "AlphaMissense.v2023.hg38"

	version("3.18.2", commit="67a154f111b4682ec03f5a059e1bda20fa506763")
	version("3.18.2", commit="67a154f111b4682ec03f5a059e1bda20fa506763")

	depends_on("r-genomicscores", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

