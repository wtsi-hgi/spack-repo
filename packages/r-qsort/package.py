# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQsort(RPackage):
	"""Scoring Q-Sort Data

	Computes scores from Q-sort data, using criteria sorts and
  derived scales from subsets of items.
  The 'qsort' package includes descriptions and scoring procedures
  for four different Q-sets commonly used in developmental psychology research:
  Attachment Q-set (version 3.0) (Waters, 1995, <doi:10.1111/j.1540-5834.1995.tb00214.x>);
  California Child Q-set (Block and Block, 1969, <doi:10.1037/0012-1649.21.3.508>);
  Maternal Behaviour Q-set (version 3.1)
  (Pederson et al., 1999, <https://ir.lib.uwo.ca/cgi/viewcontent.cgi?article=1000&context=psychologypub>);
  Preschool Q-set (Baumrind, 1968 revised by Wanda Bronson, <doi:10.1111/j.1540-5834.1995.tb00214.x>).
	"""
	
	cran = "qsort" 

	version("0.2.3", md5="3204109d62ec7ff8e44bd15a989fc8b1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
