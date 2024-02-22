# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomlca(RPackage):
	"""Random Effects Latent Class Analysis

	Fits standard and random effects latent class models. The single level random effects model is described in Qu et al <doi:10.2307/2533043> and the two level random effects model in Beath and Heller <doi:10.1177/1471082X0800900302>. Examples are given for their use in diagnostic testing.
	"""
	
	cran = "randomLCA" 

	version("1.1-3", md5="e09cb489812aafb1ec4bf0486f894200")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-fastghquad", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
