# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepfdr(RPackage):
	"""Replicability Analysis for Multiple Studies of High Dimension

	Estimation of Bayes and local Bayes false discovery rates for
      replicability analysis (Heller & Yekutieli, 2014 <doi:10.1214/13-AOAS697> ;
      Heller at al., 2015 <doi: 10.1093/bioinformatics/btu434>).
	"""
	
	homepage = "https://github.com/barakbri/repfdr"
	cran = "repfdr" 

	version("1.2.3", md5="51802fce0fce1b1da4ffdb632d6b5e27")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
