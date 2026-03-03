# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTzupdater(RPackage):
	"""Time Zone Database Updater

	Download and compile any version of the
  IANA Time Zone Database (also known as Olson database)
  and make it current in your R session.
  Beware: on Windows 'Cygwin' is required!
	"""
	
	cran = "tzupdater" 

	version("0.1.5", md5="e85518f6462f91988da1c55465ebcc0f")

