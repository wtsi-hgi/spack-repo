# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRitandata(RPackage):
	"""This package contains reference annotation and network data sets

	Data such as is contained in the two R data files in this package are required for the RITAN package examples. Users are highly encouraged to use their own or additional resources in conjunction with RITANdata. See the RITAN vignettes and RITAN.md for more information, such as gathering more up-to-date annotation data.
	"""
	
	bioc = "RITANdata"

	version("1.32.0", commit="53c06018f259350726f934b11a1d1b0fa18eed7d")
	version("1.26.0", commit="a9f3c2340e55c714ee76516ce282b7aabf93c001")

	depends_on("r@4.2:", type=("build", "run"))

