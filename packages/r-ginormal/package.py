# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGinormal(RPackage):
	"""Generalized Inverse Normal Distribution Density and Generation

	Density function and generation of random variables from the Generalized Inverse Normal (GIN) distribution from Robert (1991) <doi:10.1016/0167-7152(91)90174-P>. Also provides density functions and generation from the GIN distribution truncated to positive or negative reals. Theoretical guarantees supporting the sampling algorithms and an application to Bayesian estimation of network formation models can be found in the working paper Ding, Estrada and Montoya-Blandón (2023) <https://www.smontoyablandon.com/publication/networks/network_externalities.pdf>.
	"""
	
	homepage = "https://github.com/smonto2/ginormal"
	cran = "ginormal" 

	version("0.0.2", md5="58e86dff0f440a245e83717e1897baac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bas", type=("build", "run"))
