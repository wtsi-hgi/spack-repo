# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnm(RPackage):
	"""Supervised Normalization of Microarrays

	SNM is a modeling strategy especially designed for normalizing high-throughput genomic data. The underlying premise of our approach is that your data is a function of what we refer to as study-specific variables. These variables are either biological variables that represent the target of the statistical analysis, or adjustment variables that represent factors arising from the experimental or biological setting the data is drawn from. The SNM approach aims to simultaneously model all study-specific variables in order to more accurately characterize the biological or clinical variables of interest.
	"""
	
	bioc = "snm"

	version("1.56.0", commit="23b2403d1623aad0c31529ced6c6028f22011b30")
	version("1.50.0", commit="de889e5fd91936b50acf9afd62f7b7db7b78c510")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-lme4@1:", type=("build", "run"))
