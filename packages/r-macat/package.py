# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacat(RPackage):
	"""MicroArray Chromosome Analysis Tool

	This library contains functions to investigate links between differential gene expression and the chromosomal localization of the genes. MACAT is motivated by the common observation of phenomena involving large chromosomal regions in tumor cells. MACAT is the implementation of a statistical approach for identifying significantly differentially expressed chromosome regions. The functions have been tested on a publicly available data set about acute lymphoblastic leukemia (Yeoh et al.Cancer Cell 2002), which is provided in the library 'stjudem'.
	"""
	
	bioc = "macat" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/macat_1.76.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/macat/macat_1.76.0.tar.gz"]

	version("1.76.0", sha256="c87f4864a94ba24961c33b670a24d95ad046c1ff1ee61ae517b72b685780b4f6")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
