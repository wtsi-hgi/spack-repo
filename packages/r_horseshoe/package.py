# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHorseshoe(RPackage):
	"""Implementation of the Horseshoe Prior

	Contains functions for applying the horseshoe prior to high-
    dimensional linear regression, yielding the posterior mean and credible
    intervals, amongst other things. The key parameter tau can be equipped with
    a prior or estimated via maximum marginal likelihood estimation (MMLE).
    The main function, horseshoe, is for linear regression. In addition, there
    are functions specifically for the sparse normal means problem, allowing
    for faster computation of for example the posterior mean and posterior
    variance. Finally, there is a function available to perform variable
    selection, using either a form of thresholding, or credible intervals.
	"""
	
	cran = "horseshoe" 

	version("0.2.0", md5="674e6cbb046c0371e74df4ee6ce02c4b")

	depends_on("r@3.1:", type=("build", "run"))
