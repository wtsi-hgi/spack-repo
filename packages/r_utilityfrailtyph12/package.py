# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUtilityfrailtyph12(RPackage):
	"""Implementing EFF-TOX and Monotone Utility Based Phase 12 Trials

	Contains functions for simulating phase 12 trial designs described by Chapple and Thall (2019) including simulation and the EFF-TOX trial and simulation and implementation of the U12 trial. Functions for implementing the EFF-TOX trial are found in the package 'Phase123'.
	"""
	
	cran = "UtilityFrailtyPH12" 

	version("1.0", md5="3b6e967b1c8d2a5c534c91a87fec94ee", url="https://cran.r-project.org/src/contrib/UtilityFrailtyPH12_1.0.tar.gz")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bindata", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-phase123", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
