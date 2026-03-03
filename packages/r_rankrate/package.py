# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankrate(RPackage):
	"""Joint Statistical Models for Preference Learning with Rankings
and Ratings

	Statistical tools for the Mallows-Binomial model, the first joint statistical model for preference learning for rankings and ratings. 
	"""
	
	homepage = "https://pearce790.github.io/rankrate/"
	cran = "rankrate" 

	version("1.2.0", md5="ee3059521cbc9de4923691974c0297e0")

	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-isotone", type=("build", "run"))
