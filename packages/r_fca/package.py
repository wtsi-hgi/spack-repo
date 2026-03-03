# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFca(RPackage):
	"""Floating Catchment Area (FCA) Methods to Calculate Spatial
Accessibility

	Perform various floating catchment area methods to calculate a
    spatial accessibility index (SPAI) for demand point data. The distance
    matrix used for weighting is normalized in a preprocessing step using
    common functions (gaussian, gravity, exponential or logistic).
	"""
	
	homepage = "https://egrueebler.github.io/fca/"
	cran = "fca" 

	version("0.1.0", md5="5e3b83c828198ea817e8f2b6ffa821b3")

