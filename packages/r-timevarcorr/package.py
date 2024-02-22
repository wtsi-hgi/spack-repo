# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimevarcorr(RPackage):
	"""Time Varying Correlation

	
    Computes how the correlation between 2 time-series changes over time.
    To do so, the package follows the method from Choi & Shin (2021) <doi:10.1007/s42952-020-00073-6>.
    It performs a non-parametric kernel smoothing (using a common bandwidth) of all underlying components required for the computation of a correlation coefficient (i.e., x, y, x^2, y^2, xy).
    An automatic selection procedure for the bandwidth parameter is implemented.
    Alternative kernels can be used (Epanechnikov, box and normal).
    Both Pearson and Spearman correlation coefficients can be estimated and change in correlation over time can be tested.
	"""
	
	homepage = "https://courtiol.github.io/timevarcorr/"
	cran = "timevarcorr" 

	version("0.1.1", md5="cec8c2620a1deca01a6702c074659b53")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lpridge", type=("build", "run"))
