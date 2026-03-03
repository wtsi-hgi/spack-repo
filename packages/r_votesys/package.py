# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVotesys(RPackage):
	"""Voting Systems, Instant-Runoff Voting, Borda Method, Various
Condorcet Methods

	Various methods to count ballots in voting systems are provided.
	Functions to check validity of ballots are also provided to ensure flexibility.
	"""
	
	cran = "votesys" 

	version("0.1.1", md5="af535c56a95376499f4887a6c5107f93")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
