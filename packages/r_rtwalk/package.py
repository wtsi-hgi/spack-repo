# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtwalk(RPackage):
	"""The R Implementation of the 't-walk' MCMC Algorithm

	The 't-walk' is a general-purpose MCMC sampler for
      arbitrary continuous distributions that requires no tuning.
	"""
	
	homepage = "http://www.cimat.mx/~jac/twalk/"
	cran = "Rtwalk" 

	version("1.8.0", md5="4aeb9a65c43b2b45994060c2d13d2c70")

	depends_on("r@2.8:", type=("build", "run"))
