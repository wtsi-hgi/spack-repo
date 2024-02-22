# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeperr(RPackage):
	"""Parallelised Estimation of Prediction Error

	Designed for prediction error estimation
        through resampling techniques, possibly accelerated by parallel
        execution on a compute cluster. Newly developed model fitting
        routines can be easily incorporated. Methods used in the package are detailed in
        Porzelius Ch., Binder H. and Schumacher M. (2009) <doi:10.1093/bioinformatics/btp062>
        and were used, for instance, in
        Porzelius Ch., Schumacher M.and  Binder H. (2011) <doi:10.1007/s00180-011-0236-6>.
	"""
	
	homepage = "https://github.com/fbertran/peperr/"
	cran = "peperr" 

	version("1.5", md5="ba4ddb060e76d8487713ee5dc442d0e4")

	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
