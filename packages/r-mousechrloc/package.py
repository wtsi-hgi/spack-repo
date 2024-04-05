# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMousechrloc(RPackage):
	"""A data package containing annotation data for mouseCHRLOC

	Annotation data file for mouseCHRLOC assembled using data from public data repositories
	"""
	
	bioc = "mouseCHRLOC" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mouseCHRLOC_2.1.6.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mouseCHRLOC/mouseCHRLOC_2.1.6.tar.gz"]

	version("2.1.6", md5="0b81d7391e628cc355af4de3c5585a5f")

	depends_on("r@2.7:", type=("build", "run"))

