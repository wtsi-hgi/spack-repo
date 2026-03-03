# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectr(RPackage):
	"""Calculate the Periodogram of a Time-Course

	Provides a consistent interface to use various methods to calculate
  the periodogram and estimate the period of a rhythmic time-course. Methods
  include Lomb-Scargle, fast Fourier transform, and three versions of the
  chi-square periodogram. See Tackenberg and Hughey (2021)
  <doi:10.1371/journal.pcbi.1008567>.
	"""
	
	homepage = "https://spectr.hugheylab.org"
	cran = "spectr" 

	version("1.0.1", md5="6452cde3a7117c4b3bb058790e987dfb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table@1.12.2:", type=("build", "run"))
	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-lomb@2:", type=("build", "run"))
