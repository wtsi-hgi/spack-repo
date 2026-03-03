# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTtcg(RPackage):
	"""Three-Term Conjugate Gradient for Unconstrained Optimization

	Some accelerated three-term conjugate gradient algorithms implemented purely in R with the same user interface as optim(). The search directions and acceleration scheme are described in Andrei, N. (2013) <doi:10.1016/j.amc.2012.11.097>, Andrei, N. (2013) <doi:10.1016/j.cam.2012.10.002>, and Andrei, N (2015) <doi:10.1007/s11075-014-9845-9>. Line search is done by a hybrid algorithm incorporating the ideas in Oliveia and Takahashi (2020) <doi:10.1145/3423597> and More and Thuente (1994) <doi:10.1145/192115.192132>.
	"""
	
	homepage = "https://git.sr.ht/~hckiang/ttcg"
	cran = "ttcg" 

	version("1.0.1", md5="8c373267dfc75106bfdaab5f8d863fb4")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
