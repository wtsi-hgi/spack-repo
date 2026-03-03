# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPatternator(RPackage):
	"""Feature Extraction from Female Brown Anole Lizard Dorsal
Patterns

	Provides a set of functions to efficiently recognize and clean the continuous dorsal pattern of a female brown anole lizard (Anolis sagrei) traced from 'ImageJ', an open platform for scientific image analysis (see <https://imagej.net> for more information), and extract common features such as the pattern sinuosity indices, coefficient of variation, and max-min width.
	"""
	
	homepage = "https://github.com/stathwang/patternator"
	cran = "patternator" 

	version("0.1.0", md5="6fce681c36863546c119d66385ca0723")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
