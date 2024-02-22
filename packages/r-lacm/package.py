# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLacm(RPackage):
	"""Latent Autoregressive Count Models

	Perform pairwise likelihood inference in latent autoregressive count models. See Pedeli and Varin (2020) for details. 
	"""
	
	cran = "lacm" 

	version("0.1.1", md5="75f44c9cceb9cdd48414ff0799580654")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
