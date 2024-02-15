# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInvgamma(RPackage):
	"""The Inverse Gamma Distribution

	Light weight implementation of the standard distribution
  functions for the inverse gamma distribution, wrapping those for the gamma
  distribution in the stats package.
	"""
	
	homepage = "https://github.com/dkahle/invgamma"
	cran = "invgamma" 

	version("1.1", md5="d47d0e0a48879a43e135e8e98f10ecee")
