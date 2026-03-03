# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNltt(RPackage):
	"""Calculate the NLTT Statistic

	Provides functions to calculate the normalised Lineage-Through-
    Time (nLTT) statistic, given two phylogenetic trees. The nLTT statistic measures
    the difference between two Lineage-Through-Time curves, where each curve is
    normalised both in time and in number of lineages.
	"""
	
	homepage = "https://github.com/thijsjanzen/nLTT"
	cran = "nLTT" 

	version("1.4.9", md5="c4f7c5f0768a63ed9c055dc43e789492")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-testit", type=("build", "run"))
