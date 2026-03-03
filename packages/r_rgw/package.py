# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgw(RPackage):
	"""Goodman-Weare Affine-Invariant Sampling

	Implementation of the affine-invariant method of Goodman & Weare (2010) <DOI:10.2140/camcos.2010.5.65>, a method of producing Monte-Carlo samples from a target distribution.
	"""
	
	homepage = "https://github.com/abmantz/rgw"
	cran = "rgw" 

	version("0.3.0", md5="933f69e545dac746d7a872a360562363")

