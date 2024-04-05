# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimbenchdata(RPackage):
	"""SimBenchData: a collection of 35 single-cell RNA-seq data covering a wide range of data characteristics

	The SimBenchData package contains a total of 35 single-cell RNA-seq datasets covering a wide range of data characteristics, including major sequencing protocols, multiple tissue types, and both human and mouse sources.
	"""
	
	bioc = "SimBenchData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/SimBenchData_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/SimBenchData/SimBenchData_1.10.0.tar.gz"]

	version("1.10.0", md5="c801056ea68c668cd98230e8956d551b")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

