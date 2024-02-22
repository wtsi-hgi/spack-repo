# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVfprogression(RPackage):
	"""Visual Field (VF) Progression Analysis and Plotting Methods

	Realization of published methods to analyze visual field (VF) progression. Introduction to the plotting methods (designed by author TE) for VF output visualization. A sample dataset for two eyes, each with 10 follow-ups is included. The VF analysis methods could be found in -- Musch et al. (1999) <doi:10.1016/S0161-6420(99)90147-1>, Nouri-Mahdavi et at. (2012) <doi:10.1167/iovs.11-9021>, Schell et at. (2014) <doi:10.1016/j.ophtha.2014.02.021>, Aptel et al. (2015) <doi:10.1111/aos.12788>.
	"""
	
	cran = "vfprogression" 

	version("0.7.1", md5="a71de6c491c84a8d8412501b609d27c9")

	depends_on("r@2.10:", type=("build", "run"))
