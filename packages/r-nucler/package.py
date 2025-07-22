# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNucler(RPackage):
	"""Nucleosome positioning package for R

	Nucleosome positioning for Tiling Arrays and NGS experiments.
	"""
	
	bioc = "nucleR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/nucleR_2.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/nucleR/nucleR_2.34.0.tar.gz"]

	version("2.34.0", sha256="f700a75fd81257427f21faed3f27fa6bc8015046370a04d7aeac2b3d804e5e8a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
