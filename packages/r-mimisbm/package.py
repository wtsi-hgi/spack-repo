# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMimisbm(RPackage):
	"""Mixture of Multilayer Integrator Stochastic Block Models

	Our approach uses a  mixture of multilayer stochastic block models to group co-membership matrices with similar information into components and to partition observations into different clusters. See De Santiago (2023, ISBN: 978-2-87587-088-9).
	"""
	
	cran = "mimiSBM" 

	version("0.0.1.3", md5="e54c45ef6baa147dfc1ff417e18d8a56")

	depends_on("r-blockmodels", type=("build", "run"))
