# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RPartykit(RPackage):
	"""A Toolkit for Recursive Partytioning.

	A toolkit with infrastructure for representing, summarizing, and
	visualizing tree-structured regression and classification models. This
	unified infrastructure can be used for reading/coercing tree models from
	different sources ('rpart', 'RWeka', 'PMML') yielding objects that share
	functionality for print()/plot()/predict() methods. Furthermore, new and
	improved reimplementations of conditional inference trees (ctree()) and
	model-based recursive partitioning (mob()) from the 'party' package are
	provided based on the new infrastructure. A description of this package was
	published by Hothorn and Zeileis (2015)
	<https://jmlr.org/papers/v16/hothorn15a.html>."""

	cran = "partykit"

	license("GPL-2.0-only OR GPL-3.0-only")

	version("1.2-20", md5="ade28e819923bcc9ce94e5eae894ff04")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-libcoin@1.0.0:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-formula@1.2.1:", type=("build", "run"))
	depends_on("r-inum@1.0.0:", type=("build", "run"))
	depends_on("r-rpart@4.1.11:", type=("build", "run"))
