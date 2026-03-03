# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrthopanels(RPackage):
	"""Dynamic Panel Models with Orthogonal Reparameterization of Fixed
Effects

	Implements the orthogonal reparameterization
    approach recommended by Lancaster (2002) to estimate dynamic panel
    models with fixed effects (and optionally: panel specific
    intercepts). The approach uses a likelihood-based estimator and
    produces estimates that are asymptotically unbiased as N goes to
    infinity, with a T as low as 2.
	"""
	
	cran = "OrthoPanels" 

	version("1.2-4", md5="044e069364fd087b62a91217e4f9abbd")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
