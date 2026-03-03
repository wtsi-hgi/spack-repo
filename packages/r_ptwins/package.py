# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtwins(RPackage):
	"""Percentile Estimation of Fetal Weight for Twins by Chorionicity

	Package to Percentile estimation of fetal weight for twins by chorionicity (dichorionic-diamniotic or monochorionic-diamniotic).
	"""
	
	cran = "PTwins" 

	version("0.1.1", md5="bc99f23227dcb6878634bd0e416fd5f8")

