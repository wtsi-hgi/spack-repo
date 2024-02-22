# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgum(RPackage):
	"""Generalized Graded Unfolding Model

	An implementation of the generalized graded unfolding model (GGUM) in R, see Roberts, Donoghue, and Laughlin (2000) <doi:10.1177/01466216000241001>). It allows to simulate data sets based on the GGUM. It fits the GGUM and the GUM, and it retrieves item and person parameter estimates. Several plotting functions are available (item and test information functions; item and test characteristic curves; item category response curves). Additionally, there are some functions that facilitate the communication between R and 'GGUM2004'. Finally, a model-fit checking utility, MODFIT(), is also available.
	"""
	
	homepage = "https://github.com/jorgetendeiro/GGUM/"
	cran = "GGUM" 

	version("0.5", md5="271d5f305d18346675a74abd860d9966")

	depends_on("r-psych", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
