# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepnorm(RPackage):
	"""Stepwise normalization functions for cDNA microarrays

	Stepwise normalization functions for cDNA microarray data.
	"""
	
	homepage = "http://www.biostat.ucsf.edu/jean/"
	bioc = "stepNorm" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/stepNorm_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/stepNorm/stepNorm_1.74.0.tar.gz"]

	version("1.80.0", tag="RELEASE_3_21")
	version("1.74.0", sha256="8ababa50c39d6e40d0f7f292bea2820dd88425df0f86680fe27b72ce1f4fc612")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
