# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeve2006(RPackage):
	"""expression and CGH data on breast cancer cell lines

	Experimental organization of combined expression and CGH data
	"""
	
	bioc = "Neve2006" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Neve2006_0.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/Neve2006/Neve2006_0.40.0.tar.gz"]

	version("0.40.0", md5="1feec2f09bac8c69ba9df5ea29e7e08c", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Neve2006_0.40.0.tar.gz")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-biobase@1.14:", type=("build", "run"))
	depends_on("r-hgu133a-db", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))

