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

	version("2.26.0", tag="RELEASE_3_21")
	version("2.20.0", sha256="f4e432648968879d898570b57e9d18dc9fd3d686b122d511d554cc6e2ba219c1")

	depends_on("r@3.5:", type=("build", "run"))

