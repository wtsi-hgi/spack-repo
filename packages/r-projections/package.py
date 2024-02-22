# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProjections(RPackage):
	"""Project Future Case Incidence

	Provides functions and graphics for projecting daily incidence based on past incidence, and estimates of the serial interval and reproduction number. Projections are based on a branching process using a Poisson-distributed number of new cases per day, similar to the model used for estimating R in 'EpiEstim' or in 'earlyR', and described by Nouvellet et al. (2017) <doi:10.1016/j.epidem.2017.02.012>. The package provides the S3 class 'projections' which extends 'matrix', with accessors and additional helpers for handling, subsetting, merging, or adding these objects, as well as dedicated printing and plotting methods.
	"""
	
	homepage = "https://www.repidemicsconsortium.org/projections/"
	cran = "projections" 

	version("0.6.0", md5="efbe55ad539ac5b5958d65594f47d435")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-incidence@1.4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
