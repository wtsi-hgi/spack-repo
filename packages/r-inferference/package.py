# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInferference(RPackage):
	"""Methods for Causal Inference with Interference

	Provides methods for estimating causal effects in the presence of interference described in  B. Saul and M. Hugdens (2017) <doi:10.18637/jss.v082.i02>. Currently it implements the inverse-probability weighted (IPW) estimators proposed by E.J. Tchetgen Tchetgen and T.J. Vanderweele (2012) <doi:10.1177/0962280210386779>.
	"""
	
	cran = "inferference" 

	version("1.0.2", md5="0b58cb1a3e8b15b85852858c2a36763f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-numderiv@2012.9.1:", type=("build", "run"))
	depends_on("r-lme4@1.1.6:", type=("build", "run"))
	depends_on("r-formula@1.1.2:", type=("build", "run"))
