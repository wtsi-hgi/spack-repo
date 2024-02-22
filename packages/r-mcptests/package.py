# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcptests(RPackage):
	"""Multiples Comparisons Procedures

	Performs the execution of the main procedures of multiple 
    comparisons in the literature, Scott-Knott (1974) <http://www.jstor.org/stable/2529204>, 
    Batista (2016) <http://repositorio.ufla.br/jspui/handle/1/11466>, including graphic representations 
    and export to different extensions of its results. An additional 
    part of the package is the presence of the performance evaluation 
    of the tests (Type I error per experiment and the power). This will 
    assist the user in making the decision for the chosen test.
	"""
	
	cran = "MCPtests" 

	version("1.0.1", md5="d2836bc1b70c442c5007df9ca984f982")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-smr", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
