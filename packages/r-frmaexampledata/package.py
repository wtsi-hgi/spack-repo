# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrmaexampledata(RPackage):
	"""Frma Example Data

	Data files used by the examples in frma and frmaTools packages
	"""
	
	bioc = "frmaExampleData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/frmaExampleData_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/frmaExampleData/frmaExampleData_1.38.0.tar.gz"]

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="5b735bb44b490613a7eaef45b6be51b08169f26473fb76c0ec24da3b6504b069")

	depends_on("r@2.10:", type=("build", "run"))

