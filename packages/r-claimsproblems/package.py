# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClaimsproblems(RPackage):
	"""Analysis of Conflicting Claims

	The analysis of conflicting claims arises when an amount has to be divided among a set of agents with claims that exceed what is available. A rule is a way of selecting a  division among the claimants. This package computes the main rules introduced in the literature from the old times until nowadays. The inventory of rules covers the proportional and the adjusted proportional rules, the constrained equal awards and the constrained equal losses rules, the  constrained egalitarian, the Piniles’ and the minimal overlap rules, the random arrival and the Talmud rules. Besides, the Dominguez and Thomson and the average of awards rules are also included. All of them can be found in the book of W. Thomson (2019), 'How to divide when there isn't enough. From Aristotle, the Talmud, and Maimonides to the axiomatics of resource allocation', with the exception of the average of awards rule (Mirás Calvo et al. (2022), <doi:10.1007/s00355-022-01414-6>). In addition,  graphical diagrams allow the user to represent, among others, the set of awards, the paths of awards, and the schedules of awards of a rule, and some indexes. A good understanding of the similarities and the differences of the rules is useful for a better decision making. Therefore this package could be helpful to students, researchers and managers alike.
	"""
	
	cran = "ClaimsProblems" 

	version("0.2.1", md5="9b4e14a0aea136c1ac39d1870a889253")

	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
