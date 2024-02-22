# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDialrjars(RPackage):
	"""Required 'libphonenumber' jars for the 'dialr' Package

	Collects 'libphonenumber' jars required for the
    'dialr' package.
	"""
	
	homepage = "https://github.com/socialresearchcentre/dialrjars"
	cran = "dialrjars" 

	version("8.13.25", md5="5b75a3ab514226b2ba466c74952e0a0b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("openjdk@1.6:", type=("build", "link", "run"))
