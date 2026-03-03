# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmstimer(RPackage):
	"""'hms' Based Timer

	Tracks elapsed clock time using a `hms::hms()` scalar, which
    if running has an attribute named start that specifies the system time
    when the timer was started.  The elapsed time is the value of the
    scalar plus the difference between the current system time and the
    system time when the timer was started.
	"""
	
	cran = "hmstimer" 

	version("0.2.1", md5="7d201a79dd145c8306065f7fb6feaf61")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
