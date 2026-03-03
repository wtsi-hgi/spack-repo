# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFossilsim(RPackage):
	"""Simulation of Fossil and Taxonomy Data

	Simulating taxonomy and fossil data on phylogenetic trees under mechanistic
    models of speciation, preservation and sampling.
	"""
	
	cran = "FossilSim" 

	version("2.3.2", md5="1649a0db9f58071596e25ed651cea9d4")

	depends_on("r-ape", type=("build", "run"))
