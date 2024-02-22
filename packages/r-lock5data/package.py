# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLock5data(RPackage):
	"""Datasets for "Statistics: UnLocking the Power of Data"

	Datasets for the third edition of "Statistics: Unlocking the Power of Data" by Lock^5
    Includes version of datasets from earlier editions.
	"""
	
	cran = "Lock5Data" 

	version("3.0.0", md5="6cd51b09d37c6e7225bd9e405e1ac716")

	depends_on("r@3.5:", type=("build", "run"))
