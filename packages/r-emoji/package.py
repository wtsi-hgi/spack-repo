# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmoji(RPackage):
	"""Data and Function to Work with Emojis

	Contains data about emojis with relevant metadata, and functions
    to work with emojis when they are in strings.
	"""
	
	homepage = "https://emilhvitfeldt.github.io/emoji/"
	cran = "emoji" 

	version("15.0", md5="9988bc1448b1ec2116d2642f441f32a3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
