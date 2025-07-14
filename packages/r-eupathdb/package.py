# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REupathdb(RPackage):
	"""Provides access to pathogen annotation resources available on EuPathDB databases

	Brings together annotation resources from the various EuPathDB databases (PlasmoDB, ToxoDB, TriTrypDB, etc.) and makes them available in R using the AnnotationHub framework.
	"""
	
	homepage = "https://github.com/khughitt/EuPathDB"
	bioc = "EuPathDB"

	version("1.0.1", commit="94b4c46b23da3250aac780a25de759644e380804")
	version("1.0.1", commit="94b4c46b23da3250aac780a25de759644e380804")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodbdata", type=("build", "run"))
	depends_on("r-annotationhub@2.13.8:", type=("build", "run"))
	depends_on("r-annotationhubdata", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))

