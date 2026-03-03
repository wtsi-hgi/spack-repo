# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqhandbook(RPackage):
	"""Miscellaneous Tools for Sequence Analysis

	It provides miscellaneous sequence analysis functions for describing episodes in individual sequences, measuring association between domains in multidimensional sequence analysis (see Piccarreta (2017) <doi:10.1177/0049124115591013>), heat maps of sequence data, Globally Interdependent Multidimensional Sequence Analysis (see Robette et al (2015) <doi:10.1177/0081175015570976>), smoothing sequences for index plots (see Piccarreta (2012) <doi:10.1177/0049124112452394>), coding sequences for Qualitative Harmonic Analysis (see Deville (1982)), measuring stress from multidimensional scaling factors (see Piccarreta and Lior (2010) <doi:10.1111/j.1467-985X.2009.00606.x>), symmetrical (or canonical) Partial Least Squares (see Bry (1996)).
	"""
	
	homepage = "https://nicolas-robette.github.io/seqhandbook/"
	cran = "seqhandbook" 

	version("0.1.1", md5="70f5dd5add58833efde36ab4ebcc711d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-traminer", type=("build", "run"))
