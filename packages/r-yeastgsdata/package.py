# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYeastgsdata(RPackage):
	"""Yeast Gold Standard Data

	A collection of so-called gold (and other) standard data sets
	"""
	
	bioc = "yeastGSData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/yeastGSData_0.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/yeastGSData/yeastGSData_0.40.0.tar.gz"]

	version("0.40.0", md5="bc455a9ecd3eb2652f887026841b3c69")


