# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbcfMtme(RPackage):
	"""Item Based Collaborative Filtering for Multi-Trait and
Multi-Environment Data

	Implements the item based collaborative filtering (IBCF) method for continues phenotypes in the context of plant breeding where data are collected for various traits that were studied in various environments proposed by Montesinos-López et al. (2017) <doi:10.1534/g3.117.300309>. 
	"""
	
	homepage = "https://github.com/frahik/IBCF.MTME"
	cran = "IBCF.MTME" 

	version("1.6-0", md5="f130f4d3e84902f391f6ff1d8226f731")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lsa", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
