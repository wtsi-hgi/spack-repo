# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFssf(RPackage):
	"""Generate Fully-Sequential Space-Filling Designs Inside a Unit
Hypercube

	Provides three methods proposed by Shang and Apley (2019) <doi:10.1080/00224065.2019.1705207> to generate fully-sequential space-filling designs inside a unit hypercube. A 'fully-sequential space-filling design' means a sequence of nested designs (as the design size varies from one point up to some maximum number of points) with the design points added one at a time and such that the design at each size has good space-filling properties. Two methods target the minimum pairwise distance criterion and generate maximin designs, among which one method is more efficient when design size is large. One method targets the maximum hole size criterion and uses a heuristic to generate what is closer to a minimax design. 
	"""
	
	cran = "FSSF" 

	version("0.1.1", md5="483d271d6e9a4efe9a8e69306f463a31")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
