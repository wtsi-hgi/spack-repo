# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLic(RPackage):
	"""The LIC Criterion for Optimal Subset Selection

	The LIC criterion is to determine the most informative subsets so that the subset can retain most of the information contained in the complete data. The philosophy of the package is described in Guo G. (2022) <doi:10.1080/02664763.2022.2053949>.
	"""
	
	cran = "LIC" 

	version("0.0.2", md5="54abddae83f3edf6d93cb90624423657")

	depends_on("r@3.5:", type=("build", "run"))
