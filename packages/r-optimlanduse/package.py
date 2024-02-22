# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimlanduse(RPackage):
	"""Robust Land-Use Optimization

	Robust multi-criteria land-allocation optimization that explicitly accounts for the uncertainty of the indicators in the objective function. Solves the problem of allocating scarce land to various land-use options with regard to multiple, coequal indicators. The method aims to find the land allocation that represents the indicator composition with the best possible trade-off under uncertainty. optimLanduse includes the actual optimization procedure as described by Knoke et al. (2016) <doi:10.1038/ncomms11877> and the post-hoc calculation of the portfolio performance as presented by Gosling et al. (2020) <doi:10.1016/j.jenvman.2020.110248>.
	"""
	
	homepage = "https://github.com/Forest-Economics-Goettingen/optimLanduse/"
	cran = "optimLanduse" 

	version("1.2.1", md5="f89ac00f7df2827837e4c1dccdc4fa03")

	depends_on("r-lpsolveapi@5.5.2.0.17.7:", type=("build", "run"))
	depends_on("r-tidyr@1.1.2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-future@1.28:", type=("build", "run"))
	depends_on("r-future-apply@1.9:", type=("build", "run"))
