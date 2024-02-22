# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTramicp(RPackage):
	"""Model-Based Causal Feature Selection for General Response Types

	Extends invariant causal prediction (Peters et al., 2016, 
    <doi:10.1111/rssb.12167>) to generalized linear and transformation models 
    (Hothorn et al., 2018, <doi:10.1111/sjos.12291>).
    The methodology is described in Kook et al. (2023,
    <doi:10.48550/arXiv.2309.12833>).
	"""
	
	cran = "tramicp" 

	version("0.0-1", md5="47db3d770c244c4cfc43d285c724a196")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-tram", type=("build", "run"))
	depends_on("r-mlt", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-variables", type=("build", "run"))
	depends_on("r-basefun", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cotram", type=("build", "run"))
	depends_on("r-dhsic", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
