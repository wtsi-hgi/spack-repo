# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInzightmr(RPackage):
	"""Tools for Exploring Multiple Response Data

	Interaction and analysis of multiple response data,
    along with other tools for analysing these types of data including
    missing value analysis and calculation of standard errors for
    a range of covariance matrix results (proportions, multinomial,
    independent samples, and multiple response).
	"""
	
	homepage = "https://inzight.nz"
	cran = "iNZightMR" 

	version("2.3.0", md5="1cc5fc3a35e49c7ce00294bbc9843a62")

	depends_on("r@2.13:", type=("build", "run"))
