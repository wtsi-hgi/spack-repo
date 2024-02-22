# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCleandata(RPackage):
	"""To Inspect and Manipulate Data; and to Keep Track of This
Process

	Functions to work with data frames to prepare data for further analysis.
    The functions for imputation, encoding, partitioning, and other manipulation can produce log files to keep track of process.
	"""
	
	homepage = "https://github.com/sherrisherry/cleandata"
	cran = "cleandata" 

	version("0.3.0", md5="a87f89fe8c56049167866839b6ff570d")

	depends_on("r@3:", type=("build", "run"))
