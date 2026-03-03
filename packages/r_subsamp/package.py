# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubsamp(RPackage):
	"""Subsample Winner Algorithm for Variable Selection in Linear
Regression with a Large Number of Variables

	This subsample winner algorithm (SWA) for regression with a large-p data (X, Y) selects the important variables (or features) among the p features X in explaining the response Y.  The SWA first uses a base procedure,  here a linear regression, on each of subsamples randomly drawn from the p variables, and then computes the scores of all features, i.e., the p variables,  according to the performance of these features collected in each of the subsample analyses. It then obtains the 'semifinalist' of the features based on the resulting scores and determines the 'finalists', i.e., the important features, from the 'semifinalist'.  Fan, Sun and Qiao (2017) <http://sr2c.case.edu/swa-reg/>.
	"""
	
	cran = "subsamp" 

	version("0.1.0", md5="5556949b95d5bb710552ae326927ee84")

	depends_on("r@3.0.1:", type=("build", "run"))
