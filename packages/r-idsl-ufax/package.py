# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdslUfax(RPackage):
	"""Exhaustive Chemical Enumeration for United Formula Annotation

	A pipeline to annotate a number of peaks from the 'IDSL.IPA' peaklists using an exhaustive chemical enumeration-based approach. This package can perform elemental composition calculations using the following 15 elements : C, B, Br, Cl, K, S, Si, N, H, As, F, I, Na, O, and P.
	"""
	
	homepage = "https://github.com/idslme/idsl.ufax"
	cran = "IDSL.UFAx" 

	version("1.9.1", md5="72db8357ec01c8c3f32b20c72dc1947f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-idsl-ipa@2.7:", type=("build", "run"))
	depends_on("r-idsl-ufa", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rcppalgos", type=("build", "run"))
