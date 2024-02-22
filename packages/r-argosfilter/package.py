# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArgosfilter(RPackage):
	"""Argos Locations Filter

	Filters animal satellite tracking data obtained from the Argos system(<https://www.argos-system.org/>), following the algorithm described in Freitas et al (2008) <doi:10.1111/j.1748-7692.2007.00180.x>. It is especially indicated for telemetry studies of marine animals, where Argos locations are predominantly of low-quality.
	"""
	
	cran = "argosfilter" 

	version("0.70", md5="f06b30afd728d146b75000b6f1de2309")

	depends_on("r@3.5:", type=("build", "run"))
