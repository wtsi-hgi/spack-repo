# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCartogramr(RPackage):
	"""Continuous Cartogram

	Procedures for making continuous cartogram. Procedures available are:
     flow based cartogram (Gastner & Newman (2004) <doi:10.1073/pnas.0400280101>),
     fast flow based cartogram (Gastner, Seguy & More (2018) <doi:10.1073/pnas.1712674115>),
     rubber band based cartogram (Dougenik et al. (1985)
                        <doi:10.1111/j.0033-0124.1985.00075.x>).
	"""
	
	cran = "cartogramR" 

	version("1.0-10", md5="c801fd733631fdce96d85f855ea7fbc4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("fftw", type=("build", "link", "run"))
