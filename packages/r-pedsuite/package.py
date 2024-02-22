# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedsuite(RPackage):
	"""Easy Installation of the 'ped suite' Packages for Pedigree
Analysis

	The 'ped suite' is a collection of packages for pedigree
    analysis, covering applications in forensic genetics, medical genetics
    and more. A detailed presentation of the 'ped suite' is given in the
    book 'Pedigree Analysis in R' (Vigeland, 2021, ISBN: 9780128244302).
	"""
	
	homepage = "https://magnusdv.github.io/pedsuite/"
	cran = "pedsuite" 

	version("1.2.0", md5="f118c759b5454f8f751720a0baab3426")

	depends_on("r-forrel", type=("build", "run"))
	depends_on("r-pedprobr", type=("build", "run"))
	depends_on("r-pedtools", type=("build", "run"))
	depends_on("r-ribd", type=("build", "run"))
	depends_on("r-verbalisr", type=("build", "run"))
	depends_on("r-pedmut", type=("build", "run"))
	depends_on("r-dvir", type=("build", "run"))
	depends_on("r-ibdsim2", type=("build", "run"))
	depends_on("r-paramlink2", type=("build", "run"))
	depends_on("r-pedbuildr", type=("build", "run"))
	depends_on("r-segregatr", type=("build", "run"))
