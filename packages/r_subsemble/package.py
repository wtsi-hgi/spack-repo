# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubsemble(RPackage):
	"""An Ensemble Method for Combining Subset-Specific Algorithm Fits

	The Subsemble algorithm is a general subset ensemble prediction method, which can be used for small, moderate, or large datasets. Subsemble partitions the full dataset into subsets of observations, fits a specified underlying algorithm on each subset, and uses a unique form of k-fold cross-validation to output a prediction function that combines the subset-specific fits. An oracle result provides a theoretical performance guarantee for Subsemble. The paper, "Subsemble: An ensemble method for combining subset-specific algorithm fits" is authored by Stephanie Sapp, Mark J. van der Laan & John Canny (2014) <doi:10.1080/02664763.2013.864263>. 
	"""
	
	homepage = "https://github.com/ledell/subsemble"
	cran = "subsemble" 

	version("0.1.0", md5="4cc88843c6099dcee570996010c11c6f")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
