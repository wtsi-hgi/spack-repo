# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsmsn(RPackage):
	"""Truncated Scale Mixtures of Skew-Normal Distributions

	Return the first four moments, estimation of parameters and sample of the TSMSN distributions (Skew Normal, Skew t, Skew Slash or Skew Contaminated Normal).
	"""
	
	cran = "TSMSN" 

	version("0.0.1", md5="1f9a24c9ac57a5ba23ff86ee023384b7")

	depends_on("r-sn", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
