# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterim(RPackage):
	"""Scheduling Interim Analyses in Clinical Trials

	Allows the simulation of the recruitment and both the event and treatment phase of a clinical trial. Based on these simulations, the timing of interim analyses can be assessed.
	"""
	
	cran = "interim" 

	version("0.8.0", md5="9b61291e741e68c605af88eef604c9ad")

	depends_on("r@3.3:", type=("build", "run"))
