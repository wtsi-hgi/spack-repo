# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWsyn(RPackage):
	"""Wavelet Approaches to Studies of Synchrony in Ecology and Other
Fields

	Tools for a wavelet-based approach to analyzing spatial synchrony, principally in ecological data. Some tools will be useful for studying community synchrony. See, for instance, Sheppard et al (2016) <doi: 10.1038/NCLIMATE2991>, Sheppard et al (2017) <doi: 10.1051/epjnbp/2017000>, Sheppard et al (2019) <doi: 10.1371/journal.pcbi.1006744>.
	"""
	
	cran = "wsyn" 

	version("1.0.4", md5="df36c428c6a65c0c721f2b43b8a4db43")

	depends_on("r-fields@9.6:", type=("build", "run"))
	depends_on("r-mass@7.3.47:", type=("build", "run"))
