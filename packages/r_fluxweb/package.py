# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFluxweb(RPackage):
	"""Estimate Energy Fluxes in Food Webs

	Compute energy fluxes in trophic networks, from resources to their consumers, and can be applied to systems ranging from simple two-species interactions to highly complex food webs. It implements the approach described in Gauzens et al. (2017) <doi:10.1101/229450> to calculate energy fluxes, which are also used to calculate equilibrium stability.
	"""
	
	homepage = "https://www.biorxiv.org/content/early/2017/12/06/229450"
	cran = "fluxweb" 

	version("0.2.0", md5="bcbd17c4ca22498559f711bfc5a3f1af")

