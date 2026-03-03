# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClomial(RPackage):
	"""Infers clonal composition of a tumor

	Clomial fits binomial distributions to counts obtained from Next Gen Sequencing data of multiple samples of the same tumor. The trained parameters can be interpreted to infer the clonal structure of the tumor.
	"""
	
	bioc = "Clomial" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Clomial_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Clomial/Clomial_1.38.0.tar.gz"]

	version("1.38.0", md5="71e609b1bef40cdadcd812f99a5956e8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
