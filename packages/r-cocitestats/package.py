# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCocitestats(RPackage):
	"""Different test statistics based on co-citation.

	A collection of software tools for dealing with co-citation data.
	"""
	
	bioc = "CoCiteStats" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CoCiteStats_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CoCiteStats/CoCiteStats_1.74.0.tar.gz"]

	version("1.74.0", sha256="74a07a73abfc430e7a03986651e130afc32d5440e2a0c0b6e5969b203bc7ada1")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
