# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGg4way(RPackage):
	"""4way Plots of Differential Expression

	4way plots enable a comparison of the logFC values from two contrasts of differential gene expression. The gg4way package creates 4way plots using the ggplot2 framework and supports popular Bioconductor objects. The package also provides information about the correlation between contrasts and significant genes of interest.
	"""
	
	homepage = "https://github.com/ben-laufer/gg4way"
	bioc = "gg4way" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/gg4way_1.0.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/gg4way/gg4way_1.0.2.tar.gz"]

	version("1.0.2", md5="119c639126af675cbf7b9daf47122dc4")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
