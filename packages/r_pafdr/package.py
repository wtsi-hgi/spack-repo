# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPafdr(RPackage):
	"""Book Companion for Processing and Analyzing Financial Data with
R

	Provides access to material from the book "Processing and Analyzing Financial Data with R" by Marcelo Perlin (2017) available at <https://sites.google.com/view/pafdr/home>.
	"""
	
	cran = "pafdR" 

	version("1.0", md5="656fb6c91de78e069c5cd74754f9967f")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-exams", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
