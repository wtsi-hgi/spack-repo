# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REgsea123(RPackage):
	"""Easy and efficient ensemble gene set testing with EGSEA

	R package that supports the workflow article `Easy and efficient ensemble gene set testing with EGSEA', Alhamdoosh et al. (2017), F1000Research, 6:2010.
	"""
	
	homepage = "https://f1000research.com/articles/6-2010"
	bioc = "EGSEA123" 
	urls = ["https://www.bioconductor.org/packages/3.18/workflows/src/contrib/EGSEA123_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/workflows/src/contrib/Archive/EGSEA123/EGSEA123_1.26.0.tar.gz"]

	version("1.26.0", md5="15f05075a0399fd0de56e0d205ce02cf", url="https://www.bioconductor.org/packages/3.18/workflows/src/contrib/EGSEA123_1.26.0.tar.gz")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-egsea@1.5.2:", type=("build", "run"))
	depends_on("r-limma@3.49.2:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-illuminaio", type=("build", "run"))

