# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPetitr(RPackage):
	"""Relative Growth Rate

	Calculates the relative growth rate (RGR) of a series of individuals by building a life table and solving the Lotka-Birch equation. (See Birch, L. C. 1948. The intrinsic rate of natural increase of an insect population. - Journal of Animal Ecology 17: 15-26) <doi:10.2307/1605>.
	"""
	
	homepage = "none"
	cran = "petitr" 

	version("1.0", md5="a700869ff4c2644457b35ffd9a20bcac")

	depends_on("r@1.8:", type=("build", "run"))
