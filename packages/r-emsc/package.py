# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmsc(RPackage):
	"""Extended Multiplicative Signal Correction

	Background correction of spectral like data. Handles variations in
  scaling, polynomial baselines, interferents, constituents and replicate variation.
  Parameters for corrections are stored for further analysis, and spectra are corrected
  accordingly.
	"""
	
	homepage = "https://github.com/khliland/EMSC/"
	cran = "EMSC" 

	version("0.9.4", md5="5248c6f456d4073c257fcba6bfd51129")
	version("0.9.3", md5="7a39e1c4200283ac38e46ae6b12f34c6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
