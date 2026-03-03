# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopcor(RPackage):
	"""Correlates of Protection and Correlates of Risk Functions

	Correlates of protection (CoP) and correlates of risk (CoR) study the immune biomarkers associated with an infectious disease outcome, e.g. COVID or HIV-1 infection. This package contains shared functions for analyzing CoP and CoR, including bootstrapping procedures, competing risk estimation, and bootstrapping marginalized risks.
	"""
	
	cran = "copcor" 

	version("2023.8-27", md5="0c45d0becfd36df2d10b5403cfe0e4b6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-kyotil", type=("build", "run"))
