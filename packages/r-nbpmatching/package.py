# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbpmatching(RPackage):
	"""Functions for Optimal Non-Bipartite Matching

	Perform non-bipartite matching and matched randomization. A
    "bipartite" matching utilizes two separate groups, e.g. smokers being
    matched to nonsmokers or cases being matched to controls. A "non-bipartite"
    matching creates mates from one big group, e.g. 100 hospitals being
    randomized for a two-arm cluster randomized trial or 5000 children who
    have been exposed to various levels of secondhand smoke and are being
    paired to form a greater exposure vs. lesser exposure comparison. At the
    core of a non-bipartite matching is a N x N distance matrix for N potential
    mates. The distance between two units expresses a measure of similarity or
    quality as mates (the lower the better). The 'gendistance()' and
    'distancematrix()' functions assist in creating this. The 'nonbimatch()'
    function creates the matching that minimizes the total sum of distances
    between mates; hence, it is referred to as an "optimal" matching. The
    'assign.grp()' function aids in performing a matched randomization. Note
    bipartite matching can be performed using the prevent option in
    'gendistance()'.
	"""
	
	homepage = "https://biostat.app.vumc.org/wiki/Main/MatchedRandomization"
	cran = "nbpMatching" 

	version("1.5.4", md5="ffd1e51122e3575fe62d10e83fed6b2a")

	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
