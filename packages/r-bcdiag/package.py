# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcdiag(RPackage):
	"""Diagnostics Plots for Bicluster Data

	Diagnostic tools based on two-way
        anova and median-polish residual plots for Bicluster output
        obtained from packages; "biclust" by Kaiser et al.(2008),"isa2"
        by Csardi et al. (2010) and "fabia" by Hochreiter et al.
        (2010). Moreover, It provides visualization tools for bicluster
        output and corresponding non-bicluster rows- or columns
        outcomes.  It has also extended the idea of Kaiser et al.(2008)
        which is, extracting bicluster output in a text format, by
        adding two bicluster methods from the fabia and isa2 R
        packages.
	"""
	
	cran = "BcDiag" 

	version("1.0.10", md5="1f41293abfa6a1e60cb06fe154f605b6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fabia", type=("build", "run"))
