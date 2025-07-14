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

	version("3.13.0", commit="c114273a4a0fd01bfd5d6760e720e311a9f5219c")
	version("3.13.0", commit="c114273a4a0fd01bfd5d6760e720e311a9f5219c")

	depends_on("r-genomicscores", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

