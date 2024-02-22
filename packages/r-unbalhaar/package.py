# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnbalhaar(RPackage):
	"""Function Estimation via Unbalanced Haar Wavelets

	Top-down and bottom-up algorithms
        for nonparametric function estimation in Gaussian noise using
        Unbalanced Haar wavelets.
	"""
	
	cran = "unbalhaar" 

	version("2.1", md5="4239a628abd65a811d1f0705be4baec5")

