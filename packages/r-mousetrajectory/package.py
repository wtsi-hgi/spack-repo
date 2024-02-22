# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMousetrajectory(RPackage):
	"""Mouse Trajectory Analyses for Behavioural Scientists

	Helping psychologists and other behavioural scientists
    to analyze mouse movement (and other 2-D trajectory) data. Bundles
    together several functions that compute spatial measures (e.g., maximum
    absolute deviation, area under the curve, sample entropy) or provide a
    shorthand for procedures that are frequently used (e.g., time 
    normalization, linear interpolation, extracting initiation and movement 
    times). For more information on these dependent measures, see Wirth et al. 
    (2020) <doi:10.3758/s13428-020-01409-0>.
	"""
	
	homepage = "https://github.com/mc-schaaf/mousetRajectory"
	cran = "mousetRajectory" 

	version("0.2.1", md5="e4fb74b375829493bd4327391798b421")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-signal@0.7:", type=("build", "run"))
