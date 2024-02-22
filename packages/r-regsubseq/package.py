# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegsubseq(RPackage):
	"""Detect and Test Regular Sequences and Subsequences

	For a sequence of event occurence times, we are interested in
  finding subsequences in it that are too "regular". We define regular as being
  significantly different from a homogeneous Poisson process. The departure from
  the Poisson process is measured using a L1 distance. See Di and Perlman 2007
  for more details.
	"""
	
	cran = "regsubseq" 

	version("0.12", md5="a12483b0512c07a3dd90d5e114160a05")

	depends_on("r@2.10:", type=("build", "run"))
