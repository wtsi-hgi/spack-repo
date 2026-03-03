# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeapsofpapers(RPackage):
	"""Easily Download Heaps of PDF and CSV Files

	Makes it easy to download a large number of files such as PDF files 
    and CSV files, while automatically slowing down requests, letting you know 
    where it is up to, and adjusting for files that have already been downloaded.
	"""
	
	homepage = "https://github.com/RohanAlexander/heapsofpapers"
	cran = "heapsofpapers" 

	version("0.1.0", md5="3aaa3c7cb6ac4979209b81c27b141851")

	depends_on("r-aws-s3", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
