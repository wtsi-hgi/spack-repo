# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHumanchrloc(RPackage):
	"""A data package containing annotation data for humanCHRLOC

	Annotation data file for humanCHRLOC assembled using data from public data repositories
	"""
	
	bioc = "humanCHRLOC" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/humanCHRLOC_2.1.6.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/humanCHRLOC/humanCHRLOC_2.1.6.tar.gz"]

	version("2.1.6", sha256="f1414af5529ca0434e56a9977ced56570fdae8f4cde32e61ea8a2a89113cb2d7")

	depends_on("r@2.7:", type=("build", "run"))

