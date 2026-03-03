# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetama(RPackage):
	"""Meta-Analysis for MicroArrays

	Combination of either p-values or modified effect sizes from different
    studies to find differentially expressed genes.
	"""
	
	cran = "metaMA" 

	version("3.1.3", md5="1bb7ad55327d9da401b0cdeec73be46d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-smvar", type=("build", "run"))
