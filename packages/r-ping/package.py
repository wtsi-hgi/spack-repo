# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPing(RPackage):
	"""Probabilistic inference for Nucleosome Positioning with MNase-based or Sonicated Short-read Data

	Probabilistic inference of ChIP-Seq using an empirical Bayes mixture model approach.
	"""
	
	bioc = "PING"

	version("2.52.0", commit="04103582e3591cfb3b2c684b211b90cd09623ae4")
	version("2.46.0", commit="49706e2598a1302821781f71c9386742510e02ea")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pics", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
