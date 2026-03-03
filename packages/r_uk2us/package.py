# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUk2us(RPackage):
	"""Convert Words Between UK and US English

	Functions for converting between UK and US spellings of English words.
	"""
	
	homepage = "https://github.com/bldavies/uk2us"
	cran = "uk2us" 

	version("0.1.0", md5="73c0202f2afad2679616667aec2d5386")

	depends_on("r@2.10:", type=("build", "run"))
