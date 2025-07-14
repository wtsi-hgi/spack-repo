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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/curatedBladderData_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/curatedBladderData/curatedBladderData_1.38.0.tar.gz"]

    version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="82ae82a5ae6820b09e43f32e6b77d48bc2a3afcc473de9bf4bc025f8505d30c5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))

