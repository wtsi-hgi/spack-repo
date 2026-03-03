# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaver(RPackage):
	"""Calculate Fetch and Wave Energy

	Functions for calculating the
    fetch (length of open water distance along given directions)
    and estimating wave energy from wind and wave monitoring data.
	"""
	
	homepage = "https://github.com/pmarchand1/waver"
	cran = "waver" 

	version("0.3.0", md5="d5e78d38fc77cbfbaeb9b85d7846016d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-geosphere@1.5:", type=("build", "run"))
