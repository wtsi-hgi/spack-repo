# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdatest(RPackage):
	"""Interval Testing Procedure for Functional Data

	Implementation of the Interval Testing Procedure for functional data in different frameworks (i.e., one or two-population frameworks, functional linear models) by means of different basis expansions (i.e., B-spline, Fourier, and phase-amplitude Fourier). The current version of the package requires functional data evaluated on a uniform grid; it automatically projects each function on a chosen functional basis; it performs the entire family of multivariate tests; and, finally, it provides the matrix of the p-values of the previous tests and the vector of the corrected p-values. The functional basis, the coupled or uncoupled scenario, and the kind of test can be chosen by the user. The package provides also a plotting function creating a graphical output of the procedure: the p-value heat-map, the plot of the corrected p-values, and the plot of the functional data.
	"""
	
	cran = "fdatest" 

	version("2.1.1", md5="b56bd0f441bee4fd0936cdc30c5b8c84")

	depends_on("r-fda", type=("build", "run"))
