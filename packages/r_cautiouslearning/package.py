# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCautiouslearning(RPackage):
	"""Control Charts with Guaranteed In-Control Performance and
Cautious Parameters Learning

	Design and use of control charts for detecting mean changes 
 based on a delayed updating of the in-control parameter estimates.
 See Capizzi and Masarotto (2019) <doi:10.1080/00224065.2019.1640096> for the
 description of the method. 
	"""
	
	cran = "CautiousLearning" 

	version("1.0.1", md5="9cb9fb6366a91a0bfc261bb22f2a7538")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-spc", type=("build", "run"))
	depends_on("r-sitmo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
