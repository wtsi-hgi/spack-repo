# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrpseq(RPackage):
	"""Group Sequential Analysis of Clinical Trials

	Design of group sequential trials, including non-binding futility analysis
  at multiple time points (Gallo, Mao, and Shih, 2014, <doi:10.1080/10543406.2014.932285>).
	"""
	
	homepage = "https://sites.google.com/view/lmaowisc/"
	cran = "grpseq" 

	version("1.0", md5="7e51ab63eae7ecf6a65e4566dc7192f2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
