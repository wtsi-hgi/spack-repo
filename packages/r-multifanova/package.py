# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultifanova(RPackage):
	"""Multiple Contrast Tests for Functional Data

	The provided package implements multiple contrast tests for functional data (Munko et al., 2023, <arXiv:2306.15259>). These procedures enable us to evaluate the overall hypothesis regarding equality, as well as specific hypotheses defined by contrasts. In particular, we can perform post hoc tests to examine particular comparisons of interest. Different experimental designs are supported, e.g., one-way and multi-way analysis of variance for functional data.
	"""
	
	cran = "multiFANOVA" 

	version("0.1.0", md5="209ba9698d0aa79123f132a6d2a524ca")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gfdmcv", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
