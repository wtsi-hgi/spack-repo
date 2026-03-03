# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrmixed(RPackage):
	"""Estimate Correlations Between Repeatedly Measured Endpoints
(E.g., Reliability) Based on Linear Mixed-Effects Models

	In clinical practice and research settings in medicine and the behavioral sciences, it is often of interest to quantify the correlation of a continuous endpoint that was repeatedly measured (e.g., test-retest correlations, ICC, etc.). This package allows for estimating these correlations based on mixed-effects models. Part of this software has been developed using funding provided from the European Union's 7th Framework Programme for research, technological development and demonstration under Grant Agreement no 602552.
	"""
	
	cran = "CorrMixed" 

	version("1.1", md5="0aabfb36ae52c4e235c2928750293a12")

	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
