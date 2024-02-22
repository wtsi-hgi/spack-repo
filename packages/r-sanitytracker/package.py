# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSanitytracker(RPackage):
	"""Keeps Track of all Performed Sanity Checks

	During the preparation of data set(s) one usually performs
    some sanity checks. The idea is that irrespective of where the
    checks are performed, they are centralized by this package in order
    to list all at once with examples if a check failed.
	"""
	
	homepage = "https://github.com/MarselScheer/sanityTracker"
	cran = "sanityTracker" 

	version("0.1.0", md5="c45f40a4920eae439f32f30a5ddd6633")

	depends_on("r-data-table@1.12.2:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
