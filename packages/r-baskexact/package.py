# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaskexact(RPackage):
	"""Analytical Calculation of Basket Trial Operating Characteristics

	Analytically calculates the operating characteristics of
    single-stage and two-stage basket trials with equal sample sizes using the
	power prior design by Baumann et al. (2024) <doi:10.48550/arXiv.2309.06988>
	and the design by Fujikawa et al. (2020) <doi:10.1002/bimj.201800404>.
	"""
	
	homepage = "https://github.com/lbau7/baskexact"
	cran = "baskexact" 

	version("1.0.0", md5="1078a15f9d1ff78f15bf988653239c42")

	depends_on("r-arrangements", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
