# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCc(RPackage):
	"""Control Charts

	Tools for creating and visualizing statistical process control charts. Control charts are used for monitoring measurement processes, such as those occurring in manufacturing.  The objective is to monitor the history of such processes and flag outlying measurements: out-of-control signals.  Montgomery, D. (2009, ISBN:978-0-470-16992-6) contains an extensive discussion of the methodology.
	"""
	
	cran = "CC" 

	version("1.0", md5="a306d740b268d0dea6b75b56809d30cd")

