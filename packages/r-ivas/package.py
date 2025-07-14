# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvas(RPackage):
	"""Identification of genetic Variants affecting Alternative Splicing

	Identification of genetic variants affecting alternative splicing.
	"""
	
	bioc = "IVAS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/IVAS_2.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/IVAS/IVAS_2.22.0.tar.gz"]

	version("2.28.0", tag="RELEASE_3_21")
	version("2.22.0", sha256="77506b6d8a16e0aa043079c1227d8d688077efb382285808cb9af8073c7e82eb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-ggfortify", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
