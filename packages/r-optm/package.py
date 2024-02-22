# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptm(RPackage):
	"""Estimating the Optimal Number of Migration Edges from 'Treemix'

	The popular population genetic software 'Treemix' by
    'Pickrell and Pritchard' (2012) <DOI:10.1371/journal.pgen.1002967>
    estimates the number of migration edges on a population tree.
    However, it can be difficult to determine the number of migration
    edges to include. Previously, it was customary to stop adding migration
    edges when 99.8% of variation in the data was explained, but 'OptM'
    automates this process using an ad hoc statistic based on the
    second-order rate of change in the log likelihood.  'OptM' also
    has added functionality for various threshold modeling
    to compare with the ad hoc statistic.
	"""
	
	cran = "OptM" 

	version("0.1.6", md5="060cd27f44f41a570c5546e0bf4996aa")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-sizer@0.1.4:", type=("build", "run"))
	depends_on("r-boot@1.3.20:", type=("build", "run"))
