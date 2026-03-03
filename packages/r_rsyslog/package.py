# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsyslog(RPackage):
	"""Interface to the 'syslog' System Logger

	Functions to write messages to the 'syslog' system logger API,
  available on all 'POSIX'-compatible operating systems. Features include
  tagging messages with a priority level and application type, as well as
  masking (hiding) messages below a given priority level.
	"""
	
	homepage = "https://github.com/atheriel/rsyslog"
	cran = "rsyslog" 

	version("1.0.3", md5="a4dd97a4bfbf6de7a30b3566d997bea4")

