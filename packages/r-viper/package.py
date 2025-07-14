# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViper(RPackage):
	"""Virtual Inference of Protein-activity by Enriched Regulon analysis

	Inference of protein activity from gene expression data, including the VIPER and msVIPER algorithms
	"""
	
	bioc = "viper" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/viper_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/viper/viper_1.36.0.tar.gz"]

    version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="57830d2c08ac916d3a3d042d01e51cb29b5c68f97e7deeef17272e62b57d1221")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
