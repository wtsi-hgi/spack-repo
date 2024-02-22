# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTiteir(RPackage):
	"""Isotonic Designs for Phase 1 Trials with Late-Onset Toxicities

	Functions to design phase 1 trials using an isotonic regression based design incorporating time-to-event information. Simulation and design functions are available, which incorporate information about followup and DLTs, and apply isotonic regression to devise estimates of DLT probability.
	"""
	
	cran = "titeIR" 

	version("0.1.0", md5="dffae08dd00cd5383610f8d0ceb9990e")

	depends_on("r-iso", type=("build", "run"))
