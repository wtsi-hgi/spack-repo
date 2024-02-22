# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopdownr(RPackage):
	"""Investigation of Fragmentation Conditions in Top-Down Proteomics

	The topdownr package allows automatic and systemic investigation of fragment conditions. It creates Thermo Orbitrap Fusion Lumos method files to test hundreds of fragmentation conditions. Additionally it provides functions to analyse and process the generated MS data and determine the best conditions to maximise overall fragment coverage.
	"""
	
	homepage = "https://github.com/sgibb/topdownr/"
	bioc = "topdownr" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/topdownr_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/topdownr/topdownr_1.24.0.tar.gz"]

	version("1.24.0", md5="9aa08f9983d77f0794cd1cce6c1b8085")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics@0.20:", type=("build", "run"))
	depends_on("r-protgenerics@1.10:", type=("build", "run"))
	depends_on("r-biostrings@2.42.1:", type=("build", "run"))
	depends_on("r-s4vectors@0.12.2:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-matrix@1.4.2:", type=("build", "run"))
	depends_on("r-msnbase@2.3.10:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-mzr@2.27.5:", type=("build", "run"))
