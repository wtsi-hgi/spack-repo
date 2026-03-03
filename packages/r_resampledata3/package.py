# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResampledata3(RPackage):
	"""Data Sets for "Mathematical Statistics with Resampling and R"
(3rd Ed)

	Data sets for Chihara and Hesterberg (2022, ISBN: 978-1-119-87404-1)
    "Mathematical Statistics with Resampling in R" (3rd Ed).
	"""
	
	homepage = "https://github.com/lchihara/MathStatsResamplingR"
	cran = "resampledata3" 

	version("1.0", md5="6a1d093117ffba7f3e6dbfd05d1cb831", url="https://cran.r-project.org/src/contrib/resampledata3_1.0.tar.gz")

	depends_on("r@4.2:", type=("build", "run"))
