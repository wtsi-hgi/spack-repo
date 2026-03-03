# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpoc(RPackage):
	"""Endogenous Perturbation Analysis of Cancer

	Estimates sparse matrices A or G using fast lasso regression from mRNA transcript levels Y and CNA profiles U. Two models are provided, EPoC A where
      AY + U + R = 0
  and EPoC G where
      Y = GU + E,
  the matrices R and E are so far treated as noise. For
  details see the manual page of 'lassoshooting' and the
  article Rebecka Jörnsten, Tobias Abenius, Teresia Kling, 
  Linnéa Schmidt, Erik Johansson, Torbjörn E M Nordling, 
  Bodil Nordlander, Chris Sander, Peter Gennemark, 
  Keiko Funa, Björn Nilsson, Linda Lindahl, Sven Nelander
  (2011) <doi:10.1038/msb.2011.17>.
	"""
	
	cran = "epoc" 

	version("0.2.6-1.1", md5="35f7245a3d4ecab02a40609a02fd2ac6")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-lassoshooting@0.1.4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-irr", type=("build", "run"))
	depends_on("r-elasticnet", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
