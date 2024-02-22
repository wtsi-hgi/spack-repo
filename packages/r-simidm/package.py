# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimidm(RPackage):
	"""Simulating Oncology Trials using an Illness-Death Model

	Based on the illness-death model a large number of clinical
    trials with oncology endpoints progression-free survival (PFS) and
    overall survival (OS) can be simulated, see Meller, Beyersmann and
    Rufibach (2019) <doi:10.1002/sim.8295>.  The simulation set-up allows
    for random and event-driven censoring, an arbitrary number of
    treatment arms, staggered study entry and drop-out.  Exponentially,
    Weibull and piecewise exponentially distributed survival times can be
    generated. The correlation between PFS and OS can be calculated.
	"""
	
	homepage = "https://github.com/insightsengineering/simIDM/"
	cran = "simIDM" 

	version("0.1.0", md5="b4dabe9e983d2be4a447d06f757309f8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-mstate", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
