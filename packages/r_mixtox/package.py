# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixtox(RPackage):
	"""Dose Response Curve Fitting and Mixture Toxicity Assessment

	Curve Fitting of monotonic(sigmoidal) & non-monotonic(J-shaped) 
 dose-response data. Predicting mixture toxicity based on reference 
 models such as 'concentration addition', 'independent action', and 'generalized 
 concentration addition'.
	"""
	
	homepage = "https://github.com/ichxw/mixtox"
	cran = "mixtox" 

	version("1.4.0", md5="ebde53072f3cf0daa039db984071cce8")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
