# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPipeDesign(RPackage):
	"""Dual-Agent Dose Escalation for Phase I Trials using the PIPE
Design

	Implements the Product of Independent beta Probabilities dose Escalation (PIPE) design for dual-agent Phase I trials as described in Mander AP, Sweeting MJ (2015) <DOI:10.1002/sim.6434>.
	"""
	
	cran = "pipe.design" 

	version("0.5.1", md5="b67b59e3d2d5d88bb506e341f122bec8")

	depends_on("r-ggplot2@1.0.1:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
