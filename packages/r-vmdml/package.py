# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVmdml(RPackage):
	"""Variational Mode Decomposition Based Machine Learning Models

	Application of Variational Mode Decomposition based different Machine Learning models for univariate time series forecasting. For method details see (i) K. Dragomiretskiy and D. Zosso (2014) <doi:10.1109/TSP.2013.2288675>; (ii)  Pankaj Das (2020) <http://krishi.icar.gov.in/jspui/handle/123456789/44138>.
	"""
	
	cran = "VMDML" 

	version("0.1.1", md5="5125e46f7be7444577957651bff2535f")

	depends_on("r-vmdecomp", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-nnfor", type=("build", "run"))
