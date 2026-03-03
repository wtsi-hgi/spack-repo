# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtl(RPackage):
	"""Correlated Trait Locus Mapping

	Identification and network inference of genetic loci associated
  with correlation changes in quantitative traits (called correlated trait loci, CTLs).
  Arends et al. (2016) <doi:10.21105/joss.00087>.
	"""
	
	cran = "ctl" 

	version("1.0.0-10", md5="c9167190cd3f798bf113883753acd297")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))
