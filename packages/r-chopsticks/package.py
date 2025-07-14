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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/chopsticks_1.68.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/chopsticks/chopsticks_1.68.0.tar.gz"]

    version("1.74.0", tag="RELEASE_3_21")
	version("1.68.0", sha256="5fe024c809302807edf170ad1108e25519b240415c25a7a2efb8584e91e0880b")

	depends_on("r-survival", type=("build", "run"))
