# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnetime(RPackage):
	"""Run Code Only Once

	Allows code to be run only once on a given computer, using
  lockfiles. Typical use cases include startup messages shown only when a
  package is loaded for the very first time.
	"""
	
	homepage = "https://github.com/hughjonesd/onetime"
	cran = "onetime" 

	version("0.2.0", md5="17aaa9eecf28270dc4091c4ca38e55c4")

	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-filelock", type=("build", "run"))
