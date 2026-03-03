# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToolmark(RPackage):
	"""Tests for Same-Source of Toolmarks

	Implements two tests for same-source of toolmarks. The chumbley_non_random() test follows the paper "An Improved Version of a Tool Mark Comparison Algorithm" by Hadler and Morris (2017) <doi:10.1111/1556-4029.13640>. This is an extension of the Chumbley score as previously described in "Validation of Tool Mark Comparisons Obtained Using a Quantitative, Comparative, Statistical Algorithm" by Chumbley et al (2010) <doi:10.1111/j.1556-4029.2010.01424.x>. fixed_width_no_modeling() is based on correlation measures in a diamond shaped area of the toolmark as described in Hadler (2017).
	"""
	
	cran = "toolmaRk" 

	version("0.0.1", md5="d4dc00d1e3865b46db496ecc33557e1c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7.2:", type=("build", "run"))
	depends_on("r-reshape2@1.4.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
