# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLifeinsurancecontracts(RPackage):
	"""Framework for Traditional Life Insurance Contracts

	Use of this package is deprecated.  It has been renamed to 'LifeInsureR'.
	"""
	
	homepage = "https://gitlab.open-tools.net/R/LifeInsureR"
	cran = "LifeInsuranceContracts" 

	version("0.0.6", md5="ec37f05af8584704f8a14a4b1ab5fc98")

	depends_on("r-lifeinsurer", type=("build", "run"))
