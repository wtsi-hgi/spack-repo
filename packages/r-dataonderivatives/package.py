# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataonderivatives(RPackage):
	"""Easily Source Publicly Available Data on Derivatives

	Post Global Financial Crisis derivatives reforms have lifted
    the veil off over-the-counter (OTC) derivative markets. Swap Execution
    Facilities (SEFs) and Swap Data Repositories (SDRs) now publish data
    on swaps that are traded on or reported to those facilities
    (respectively). This package provides you the ability to get this data
    from supported sources.
	"""
	
	homepage = "https://github.com/imanuelcostigan/dataonderivatives"
	cran = "dataonderivatives" 

	version("0.4.0", md5="091f91b1d91cd13b531fa1534706739b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vetr", type=("build", "run"))
