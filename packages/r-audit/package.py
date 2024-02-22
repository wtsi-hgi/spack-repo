# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAudit(RPackage):
	"""Bounds for Accounting Populations

	Find an upper bound for the total amount of overstatement
    of assets in a set of accounts, or estimate the amount of sales tax
    owed on a collection of transactions (Meeden and Sargent, 2007,
    <doi:10.1080/03610920701386802>).
	"""
	
	cran = "audit" 

	version("0.1-2", md5="c4f8b5106cfd8216f2eb7935b5ec92ea")

