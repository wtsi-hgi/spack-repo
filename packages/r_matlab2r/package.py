# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatlab2r(RPackage):
	"""Translation Layer from MATLAB to R

	Allows users familiar with MATLAB to use MATLAB-named functions in
    R. Several basic MATLAB functions are written in this package to mimic the
    behavior of their original counterparts, with more to come as this package
    grows.
	"""
	
	homepage = "https://ocbe-uio.github.io/matlab2r/"
	cran = "matlab2r" 

	version("1.5.0", md5="af322cd755fa744d48932e6ceae4a12b")

	depends_on("r-styler", type=("build", "run"))
