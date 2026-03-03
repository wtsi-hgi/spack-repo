# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDerfinderdata(RPackage):
	"""Processed BigWigs from BrainSpan for examples

	Processed 22 samples from BrainSpan keeping only the information for chromosome 21. Data is stored in the BigWig format and is used for examples in other packages.
	"""
	
	homepage = "https://github.com/leekgroup/derfinderData"
	bioc = "derfinderData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/derfinderData_2.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/derfinderData/derfinderData_2.20.0.tar.gz"]

	version("2.20.0", md5="032efff51d29eae3fc1a5e032c0f3c40")

	depends_on("r@3.5:", type=("build", "run"))

