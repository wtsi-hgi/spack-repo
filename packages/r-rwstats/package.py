# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwstats(RPackage):
	"""Chinese Character Frequency in Real World

	It contains Chinese character frequency data based on 
    news data from 2017 to 2019. Source of these news include Sina, China daily and Tencent.
	"""
	
	cran = "rwstats" 

	version("0.1", md5="672ca9f2503d8b840baff60154dea0b0")

	depends_on("r@3.3.2:", type=("build", "run"))
