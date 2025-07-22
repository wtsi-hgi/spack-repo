# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnotationtools(RPackage):
	"""Annotate microarrays and perform cross-species gene expression analyses using flat file databases

	Functions to annotate microarrays, find orthologs, and integrate heterogeneous gene expression profiles using annotation and other molecular biology information available as flat file database (plain text files).
	"""
	
	bioc = "annotationTools" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/annotationTools_1.76.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/annotationTools/annotationTools_1.76.0.tar.gz"]

	version("1.76.0", sha256="4ea31896f495b577d95d72d1ba8ad87f05e6036fc6f44f04537c4c036436083c")

	depends_on("r-biobase", type=("build", "run"))
