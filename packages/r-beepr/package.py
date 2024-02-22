# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeepr(RPackage):
	"""Easily Play Notification Sounds on any Platform

	The main function of this package is beep(), with the purpose to
    make it easy to play notification sounds on whatever platform you are on.
    It is intended to be useful, for example, if you are running a long analysis
    in the background and want to know when it is ready.
	"""
	
	cran = "beepr" 

	version("1.3", md5="134a9da416612bd137acd7522fd2f65c")

	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-audio", type=("build", "run"))
