# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSocialranking(RPackage):
	"""Social Ranking Solutions for Power Relations on Coalitions

	The notion of power index has been widely used in literature to evaluate the influence of individual players (e.g., voters, political parties, nations, stockholders, etc.) involved in a collective decision situation like an electoral system, a parliament, a council, a management board, etc., where players may form coalitions. Traditionally this ranking is determined through numerical evaluation. More often than not however only ordinal data between coalitions is known. The package 'socialranking' offers a set of solutions to rank players based on a transitive ranking between coalitions, including through CP-Majority, ordinal Banzhaf or lexicographic excellence solution summarized by Tahar Allouche, Bruno Escoffier, Stefano Moretti and Meltem Öztürk (2020, <doi:10.24963/ijcai.2020/3>).
	"""
	
	homepage = "https://github.com/jassler/socialranking"
	cran = "socialranking" 

	version("1.1.0", md5="4a64aab67a562a1193ba7afa427513fe")

	depends_on("r-relations@0.6.13:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-rdpack@2.4:", type=("build", "run"))
