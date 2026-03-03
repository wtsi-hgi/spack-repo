# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpistemicgametheory(RPackage):
	"""Constructing an Epistemic Model for the Games with Two Players

	Constructing an epistemic model such that, for every player i and for every choice c(i) which is optimal, there is one type that expresses common belief in rationality.
	"""
	
	cran = "EpistemicGameTheory" 

	version("0.1.2", md5="6ab56a1368fa7be80e389e39c79cbd90")

	depends_on("r-lpsolve", type=("build", "run"))
