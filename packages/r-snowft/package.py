# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnowft(RPackage):
	"""Fault Tolerant Simple Network of Workstations

	Extension of the snow package supporting fault tolerant and reproducible applications, as well as supporting easy-to-use parallel programming - only one function is needed. Dynamic cluster size is also available.
	"""
	
	homepage = "http://www.stat.washington.edu/hana/parallel/snowFT-doc.pdf"
	cran = "snowFT" 

	version("1.6-1", md5="51cc5eeeb2fdae2d0c6560423a8368c4")

	depends_on("r@3.0.0:", type=("build", "run"))
	depends_on("r-rlecuyer", type=("build", "run"))
	depends_on("r-snow@0.4:", type=("build", "run"))
