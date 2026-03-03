# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArules(RPackage):
	"""Mining Association Rules and Frequent Itemsets

	Provides the infrastructure for representing, manipulating and analyzing 
  transaction data and patterns (frequent itemsets and association rules). 
  Also provides C implementations of the association mining algorithms Apriori and Eclat. 
  Hahsler, Gruen and Hornik (2005) <doi:10.18637/jss.v014.i15>.
	"""
	
	homepage = "https://github.com/mhahsler/arules"
	cran = "arules" 

	version("1.7-7", md5="047c716f398ca60fdf0f71a9e547b046")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix@1.4.0:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
