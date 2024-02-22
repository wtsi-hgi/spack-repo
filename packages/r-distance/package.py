# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistance(RPackage):
	"""Distance Sampling Detection Function and Abundance Estimation

	A simple way of fitting detection functions to distance sampling
    data for both line and point transects. Adjustment term selection, left and
    right truncation as well as monotonicity constraints and binning are
    supported. Abundance and density estimates can also be calculated (via a
    Horvitz-Thompson-like estimator) if survey area information is provided. See
    Miller et al. (2019) <doi:10.18637/jss.v089.i01> for more information on
    methods and <https://examples.distancesampling.org/> for example analyses.
	"""
	
	homepage = "https://github.com/DistanceDevelopment/Distance/"
	cran = "Distance" 

	version("1.0.9", md5="fbeb3fa146cd97cff2149bfd616667af")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mrds@2.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
