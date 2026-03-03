# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmofit(RPackage):
	"""Advanced L-Moment Fitting of Distributions

	A complete framework for frequency analysis is provided by 'LMoFit'. It has functions related to the determination of sample L-moments as in Hosking, J.R.M. (1990) <doi:10.1111/j.2517-6161.1990.tb01775.x>, the fitting of various distributions as in Zaghloul et al. (2020) <doi:10.1016/j.advwatres.2020.103720> and Hosking, J.R.M. (2019) <https://CRAN.R-project.org/package=lmom>, besides plotting and manipulating L-space diagrams as in Papalexiou, S.M. & Koutsoyiannis, D. (2016) <doi:10.1016/j.advwatres.2016.05.005> for two-shape parametric distributions on the L-moment ratio diagram. Additionally, the quantile, probability density, and cumulative probability functions of various distributions are provided in a user-friendly manner.
	"""
	
	cran = "LMoFit" 

	version("0.1.6", md5="e71f825a16f14d1f53cd562ea72838d9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-lmom", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
