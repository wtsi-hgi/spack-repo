# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGroupica(RPackage):
	"""Independent Component Analysis for Grouped Data

	Contains an implementation of an independent component analysis (ICA) for grouped data. The main function groupICA() performs a blind source separation, by maximizing an independence across sources and allows to adjust for varying confounding for user-specified groups. Additionally, the package contains the function uwedge() which can be used to approximately jointly diagonalize a list of matrices. For more details see the project website <https://sweichwald.de/groupICA/>.
	"""
	
	homepage = "https://github.com/sweichwald/groupICA-R"
	cran = "groupICA" 

	version("0.1.1", md5="5b25dd7f8df8df2c2045ec23753a2458")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
