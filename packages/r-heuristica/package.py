# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeuristica(RPackage):
	"""Heuristics Including Take the Best and Unit-Weight Linear

	Implements various heuristics like Take The Best and
    unit-weight linear, which do two-alternative choice: which of
    two objects will have a higher criterion?  Also offers functions
    to assess performance, e.g. percent correct across all row pairs
    in a data set and finding row pairs where models disagree.
    New models can be added by implementing a fit and predict function--
    see vignette.  Take The Best was first described in: Gigerenzer, G.
    & Goldstein, D. G. (1996) <doi:10.1037/0033-295X.103.4.650>.  All
    of these heuristics were run on many data sets and analyzed in:
    Gigerenzer, G., Todd, P. M., & the ABC Group (1999).
    <ISBN:978-0195143812>.
	"""
	
	homepage = "https://github.com/jeanimal/heuristica"
	cran = "heuristica" 

	version("1.0.3", md5="8127c9d6930d1733a435a38e49404c92")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
