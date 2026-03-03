# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopulr(RPackage):
	"""Population Downscaling Using Areal Interpolation

	Given a 
    set of source zone polygons such as
    census tracts or city blocks alongside with population counts and a 
    target zone of incogruent yet superimposed polygon features (such as
    individual buildings) populR transforms population counts from the 
    former to the latter using Areal Interpolation methods.
	"""
	
	homepage = "https://github.com/mbatsaris/populR/"
	cran = "populR" 

	version("0.2.1", md5="12b0531c89f8b37a132d6601139141f2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-osmdata", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
