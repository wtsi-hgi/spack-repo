# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocbook(RPackage):
	"""Write, containerize, publish and version Quarto books with Bioconductor

	A BiocBook can be created by authors (e.g. R developers, but also scientists, teachers, communicators, ...) who wish to 1) write (compile a body of biological and/or bioinformatics knowledge), 2) containerize (provide Docker images to reproduce the examples illustrated in the compendium), 3) publish (deploy an online book to disseminate the compendium), and 4) version (automatically generate specific online book versions and Docker images for specific Bioconductor releases).
	"""
	
	homepage = "https://bioconductor.org/packages/BiocBook"
	bioc = "BiocBook" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BiocBook_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BiocBook/BiocBook_1.0.0.tar.gz"]

	version("1.0.0", md5="6bcb226068f30b135b705960de603ff0")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-available", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-gert", type=("build", "run"))
	depends_on("r-gh", type=("build", "run"))
	depends_on("r-gitcreds", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-quarto", type=("build", "run"))
	depends_on("r-renv", type=("build", "run"))
