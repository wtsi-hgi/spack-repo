# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArulessequences(RPackage):
	"""Mining Frequent Sequences

	Add-on for arules to handle and mine frequent sequences.
    Provides interfaces to the C++ implementation of cSPADE by  
    Mohammed J. Zaki.
	"""
	
	cran = "arulesSequences" 

	version("0.2-30", md5="1d10db7a1b48ef75b810a4c41160d73b")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-arules@1.5.1:", type=("build", "run"))
