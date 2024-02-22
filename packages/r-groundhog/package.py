# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGroundhog(RPackage):
	"""Version-Control for CRAN, GitHub, and GitLab Packages

	Make R scripts reproducible, by ensuring that
    every time a given script is run, the same version of the used packages are
    loaded (instead of whichever version the user running the script happens to
    have installed). This is achieved by using the command
    groundhog.library() instead of the base command library(), and including a
    date in the call. The date is used to call on the same version of the
    package every time (the most recent version available at that date).
    Load packages  from CRAN, GitHub, or Gitlab.
	"""
	
	homepage = "https://groundhogr.com/"
	cran = "groundhog" 

	version("3.2.0", md5="c6d774a816c47034675afbe27083b2e7")

