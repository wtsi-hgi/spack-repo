# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedbladderdata(RPackage):
	"""Bladder Cancer Gene Expression Analysis

	The curatedBladderData package provides relevant functions and data for gene expression analysis in patients with bladder cancer.
	"""
	
	homepage = "https://github.com/lima1/curatedBladderData"
	bioc = "curatedBladderData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/curatedBladderData_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/curatedBladderData/curatedBladderData_1.38.0.tar.gz"]

	version("1.38.0", md5="bd8965c4ad49840b4985f90f3dc5a441")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))

	# experiment