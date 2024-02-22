# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFptdapprox(RPackage):
	"""Approximation of First-Passage-Time Densities for Diffusion
Processes

	Efficient approximation of first passage time densities for diffusion processes based on the First Passage Time Location (FPTL) function.
	"""
	
	cran = "fptdApprox" 

	version("2.5", md5="75f4f04a0e2f13f159f80aa463245487")

