# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRapidphylo(RPackage):
	"""Rapidly Estimates Phylogeny from Large Allele Frequency Data
Using Root Distances Method

	Rapidly estimates tree-topology from large allele frequency
    data using Root Distances Method, under a Brownian Motion Model. See
    Peng et al. (2021) <doi:10.1016/j.ympev.2021.107142>.
	"""
	
	homepage = "https://github.com/ArindamRoyChoudhury/rapidphylo"
	cran = "rapidphylo" 

	version("0.1.2", md5="7c11c554de80c10dd124fa75e5e48d1c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
