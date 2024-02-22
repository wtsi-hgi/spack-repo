# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHem(RPackage):
	"""Heterogeneous error model for identification of differentially expressed genes under multiple conditions

	This package fits heterogeneous error models for analysis of microarray data
	"""
	
	homepage = "http://www.healthsystem.virginia.edu/internet/hes/biostat/bioinformatics/"
	bioc = "HEM" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/HEM_1.74.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/HEM/HEM_1.74.0.tar.gz"]

	version("1.74.0", md5="3ad1825d95504eaf9e2bcad8438816f5")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
