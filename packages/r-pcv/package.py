# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcv(RPackage):
	"""Procrustes Cross-Validation

	Implements Procrustes cross-validation method for Principal Component Analysis, Principal Component Regression and Partial Least Squares regression models. S. Kucheryavskiy (2023) <doi:10.1016/j.aca.2023.341096>.
	"""
	
	homepage = "https://github.com/svkucheryavski/pcv"
	cran = "pcv" 

	version("1.1.0", md5="c6e91c90ee020595a037ec9970bd34db")

	depends_on("r@3.5:", type=("build", "run"))
