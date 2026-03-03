# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCem(RPackage):
	"""Coarsened Exact Matching

	Implementation of the Coarsened Exact Matching algorithm discussed 
	along with its properties in
  Iacus, King, Porro (2011) <DOI:10.1198/jasa.2011.tm09599>;
	Iacus, King, Porro (2012) <DOI:10.1093/pan/mpr013> and
	Iacus, King, Porro (2019) <DOI:10.1017/pan.2018.29>.
	"""
	
	homepage = "https://gking.harvard.edu/cem"
	cran = "cem" 

	version("1.1.31", md5="4c26112b5f74267a3d6b946dd7ae0cc7")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-matchit", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
