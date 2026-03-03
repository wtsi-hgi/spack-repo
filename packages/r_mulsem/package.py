# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulsem(RPackage):
	"""Some Multivariate Analyses using Structural Equation Modeling

	A set of functions for some multivariate analyses utilizing a
             structural equation modeling (SEM) approach through the 'OpenMx' package.
             These analyses include canonical correlation analysis (CANCORR),
             redundancy analysis (RDA), and multivariate principal component regression (MPCR).
             It implements procedures discussed in Gu and Cheung (2023) <doi:10.1111/bmsp.12301>,
             Gu, Yung, and Cheung (2019) <doi:10.1080/00273171.2018.1512847>, and
             Gu et al. (2023) <doi:10.1080/00273171.2022.2141675>.
	"""
	
	homepage = "https://github.com/mikewlcheung/mulsem"
	cran = "mulSEM" 

	version("1.0", md5="49b4c3f12adc8d04feebe24c878e3be8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-openmx", type=("build", "run"))
