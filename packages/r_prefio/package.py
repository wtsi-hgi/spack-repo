# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrefio(RPackage):
	"""Structures for Preference Data

	Convenient structures for creating, sourcing, reading, writing
  and manipulating ordinal preference data. Methods for writing to/from PrefLib
  formats. See Nicholas Mattei and Toby Walsh "PrefLib: A Library of Preference
  Data" (2013) <doi:10.1007/978-3-642-41575-3_20>.
	"""
	
	homepage = "https://github.com/fleverest/prefio/"
	cran = "prefio" 

	version("0.1.1", md5="5e88a7092b3aec56caa8115a2e7486da")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
