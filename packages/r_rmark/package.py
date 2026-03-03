# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmark(RPackage):
	"""R Code for Mark Analysis

	An interface to the software package MARK that constructs input
    files for MARK and extracts the output. MARK was developed by Gary White
    and is freely available at <http://www.phidot.org/software/mark/downloads/>
    but is not open source.
	"""
	
	cran = "RMark" 

	version("3.0.0", md5="f8e411ddd1d03f4ec5982c550d576a77")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
