# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrwarp(RPackage):
	"""Warping Landmark Configurations

	Compute bending energies, principal warps, partial warp scores, and the non-affine component of shape variation for 2D landmark configurations, as well as Mardia-Dryden distributions and self-similar distributions of landmarks, as described in Mitteroecker et al. (2020) <doi:10.1093/sysbio/syaa007>. Working examples to decompose shape variation into small-scale and large-scale components, and to decompose the total shape variation into outline and residual shape components are provided. Two landmark datasets are provided, that quantify skull morphology in humans and papionin primates, respectively from Mitteroecker et al. (2020) <doi:10.5061/dryad.j6q573n8s> and Grunstra et al. (2020) <doi:10.5061/dryad.zkh189373>. 
	"""
	
	cran = "prWarp" 

	version("1.0.1", md5="041693f74374f4aff27304c3ea1eacb9")
	version("1.0.0", md5="86588fcbd4639643ddfaf8a25b2e18a8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-morpho", type=("build", "run"))
