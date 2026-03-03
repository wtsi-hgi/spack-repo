# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfmta(RPackage):
	"""Phase I/II Adaptive Dose-Finding Design for MTA

	Phase I/II adaptive dose-finding design for single-agent
   Molecularly Targeted Agent (MTA), according to the paper "Phase
   I/II Dose-Finding Design for Molecularly Targeted Agent: Plateau
   Determination using Adaptive Randomization", Riviere Marie-Karelle et
   al. (2016) <doi:10.1177/0962280216631763>.
	"""
	
	cran = "dfmta" 

	version("1.7-3", md5="0eab9d0555fc1541ec758a0003b4d1ec")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.100.3.1:", type=("build", "run"))
	depends_on("r-bh@1.55:", type=("build", "run"))
	depends_on("r-rcppprogress@0.2.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
