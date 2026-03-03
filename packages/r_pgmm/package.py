# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgmm(RPackage):
	"""Parsimonious Gaussian Mixture Models

	Carries out model-based clustering or classification using parsimonious Gaussian mixture models. McNicholas and Murphy (2008) <doi:10.1007/s11222-008-9056-0>, McNicholas (2010) <doi:10.1016/j.jspi.2009.11.006>, McNicholas and Murphy (2010) <doi:10.1093/bioinformatics/btq498>, McNicholas et al. (2010) <doi:10.1016/j.csda.2009.02.011>.
	"""
	
	cran = "pgmm" 

	version("1.2.7", md5="525c4f2b656afa45e39ddc6b2b66d972")

