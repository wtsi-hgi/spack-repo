# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensitivitycasecontrol(RPackage):
	"""Sensitivity Analysis for Case-Control Studies

	Sensitivity analysis for case-control studies in which some cases may meet a more narrow definition of being a case compared to other cases which only meet a broad definition.  The sensitivity analyses are described in Small, Cheng, Halloran and Rosenbaum (2013, "Case Definition and Sensitivity Analysis", Journal of the American Statistical Association, 1457-1468).  The functions sens.analysis.mh and sens.analysis.aberrant.rank provide sensitivity analyses based on the Mantel-Haenszel test statistic and aberrant rank test statistic as described in Rosenbaum (1991, "Sensitivity Analysis for Matched Case Control Studies", Biometrics); see also Section 1 of Small et al.  The function adaptive.case.test provides adaptive inferences as described in Section 5 of Small et al.  The function adaptive.noether.brown provides a sensitivity analysis for a matched cohort study based on an adaptive test.  The other functions in the package are internal functions.  
	"""
	
	cran = "SensitivityCaseControl" 

	version("2.2", md5="940e190aefa9db25cec3ee34e46a4333")

