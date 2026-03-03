# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimeless(RPackage):
	"""Fast General Purpose Date/Time Converter

	Fast general purpose date/time converter using 'Rust'. The package implements date time, date and epoch time parser for heterogeneous vectors of dates.
	"""
	
	homepage = "https://github.com/schochastics/timeless"
	cran = "timeless" 

	version("0.2.1", md5="336fec6974a8c02b268b3366e06c4f70")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("rust", type=("build", "link", "run"))
