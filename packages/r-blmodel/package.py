# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlmodel(RPackage):
	"""Black-Litterman Posterior Distribution

	Posterior distribution in the Black-Litterman model is computed from a prior distribution given in the form of a time series of asset returns and a continuous distribution of views provided by the user as an external function.
	"""
	
	cran = "BLModel" 

	version("1.0.2", md5="1dd3b5c456e13a3f15716d857e7f205c")

	depends_on("r@3.3:", type=("build", "run"))
