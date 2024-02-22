# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChopsticks(RPackage):
	"""The 'snp.matrix' and 'X.snp.matrix' Classes

	Implements classes and methods for large-scale SNP association studies
	"""
	
	homepage = "http://outmodedbonsai.sourceforge.net/"
	bioc = "chopsticks" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/chopsticks_1.68.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/chopsticks/chopsticks_1.68.0.tar.gz"]

	version("1.68.0", md5="b63b111068a6d42f7812010d1dc31047")

	depends_on("r-survival", type=("build", "run"))
