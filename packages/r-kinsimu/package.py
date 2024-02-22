# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKinsimu(RPackage):
	"""Panel Evaluation in Forensic Kinship Analysis

	Evaluate specific panels in different aspects: i) Simulation tools related to pedigree researches; ii) calculation for systemic effectiveness indicators, such as probability of exclusion (PE).
	"""
	
	cran = "KINSIMU" 

	version("0.1.2", md5="ea4d7bce063f52b0f3d96fe4518a1fda")

	depends_on("r@3.5:", type=("build", "run"))
