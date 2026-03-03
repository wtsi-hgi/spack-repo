# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoint(RPackage):
	"""Protein Structure Guided Local Test

	Provides an implementation of a rare variant association test that utilizes protein tertiary structure to increase signal and to identify likely causal variants. Performs structure-guided collapsing, which leads to local tests that borrow information from neighboring variants on a protein and that provide association information on a variant-specific level. For details of the implemented method see West, R. M.,  Lu, W., Rotroff, D. M., Kuenemann, M., Chang, S-M., Wagner M. J., Buse, J. B., Motsinger-Reif, A., Fourches, D., and Tzeng, J-Y. (2019) <doi:10.1371/journal.pcbi.1006722>.
	"""
	
	cran = "POINT" 

	version("1.3", md5="9fc2145668e8728dcbb36509d3e3cd42")

	depends_on("r-rarpack", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
