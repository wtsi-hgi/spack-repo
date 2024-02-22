# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGnorm(RPackage):
	"""Generalized Normal/Exponential Power Distribution

	Functions for obtaining generalized normal/exponential power distribution probabilities, quantiles, densities and random deviates. The generalized normal/exponential power distribution was introduced by Subbotin (1923) and rediscovered by Nadarajah (2005). The parametrization given by Nadarajah (2005) <doi:10.1080/02664760500079464> is used.
	"""
	
	homepage = "http://github.com/maryclare/gnorm"
	cran = "gnorm" 

	version("1.0.0", md5="77860053c6b31b281801e89977cd7a67")

