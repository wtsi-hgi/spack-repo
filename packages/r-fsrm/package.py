# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsrm(RPackage):
	"""Social Relations Analyses with Roles ("Family SRM")

	Social Relations Analysis with roles ("Family SRM") are computed,
    using a structural equation modeling approach. Groups ranging from three members
    up to an unlimited number of members are supported and the mean structure can
    be computed. Means and variances can be compared between different groups of
    families and between roles.
	"""
	
	cran = "fSRM" 

	version("0.6.5", md5="9d226ef9b2a9654965882804e2ea0785")

	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
