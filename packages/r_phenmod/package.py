# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenmod(RPackage):
	"""Auxiliary Functions for Phenological Data Processing, Modelling
and Result Handling

	Provides functions for phenological data preprocessing, modelling and result handling. For more information, please refer to Lange et al. (2016) <doi:10.1007/s00484-016-1161-8>.
	"""
	
	cran = "phenmod" 

	version("1.2-7", md5="10c964caff15310fec71f3ba5332dff7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-pheno", type=("build", "run"))
