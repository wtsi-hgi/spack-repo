# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdpcrclust(RPackage):
	"""Clustering algorithm for ddPCR data

	The ddPCRclust algorithm can automatically quantify the CPDs of non-orthogonal ddPCR reactions with up to four targets. In order to determine the correct droplet count for each target, it is crucial to both identify all clusters and label them correctly based on their position. For more information on what data can be analyzed and how a template needs to be formatted, please check the vignette.
	"""
	
	homepage = "https://github.com/bgbrink/ddPCRclust"
	bioc = "ddPCRclust" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ddPCRclust_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ddPCRclust/ddPCRclust_1.22.0.tar.gz"]

    version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="4c745a4fbe80d7827e24e9ccfbb911a61aa636fba5a46aadf6de862667f1cd31")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowdensity@1.13.3:", type=("build", "run"))
	depends_on("r-samspectral", type=("build", "run"))
	depends_on("r-flowpeaks", type=("build", "run"))
