# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFakmct(RPackage):
	"""Fuzzy Adaptive Resonance Theory K-Means Clustering Technique

	A set of function for clustering data observation with hybrid method Fuzzy ART and K-Means 
            by Sengupta, Ghosh & Dan (2011) <doi:10.1080/0951192X.2011.602362>.
	"""
	
	homepage = "<https://github.com/alfinurrahmah/fakmct>"
	cran = "fakmct" 

	version("0.1.0", md5="a06373ec5179ebe7ae40ea17b78dc7f6")

	depends_on("r@3.5:", type=("build", "run"))
