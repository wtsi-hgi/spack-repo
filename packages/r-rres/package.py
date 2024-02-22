# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRres(RPackage):
	"""Realized Relatedness Estimation and Simulation

	Functions for studying realized genetic relatedness between people. Users will be able to simulate inheritance patterns given pedigree structures, generate SNP marker data given inheritance patterns, and estimate realized relatedness between pairs of individuals using SNP marker data. See Wang (2017) <doi:10.1534/genetics.116.197004>. This work was supported by National Institutes of Health grants R37 GM-046255.
	"""
	
	cran = "rres" 

	version("1.1", md5="c7371028e4c500c3e62911983911ea44")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
