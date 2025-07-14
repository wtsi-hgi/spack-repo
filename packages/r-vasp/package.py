# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVasp(RPackage):
	"""Quantification and Visualization of Variations of Splicing in Population

	Discovery of genome-wide variable alternative splicing events from short-read RNA-seq data and visualizations of gene splicing information for publication-quality multi-panel figures in a population. (Warning: The visualizing function is removed due to the dependent package Sushi deprecated. If you want to use it, please change back to an older version.)
	"""
	
	homepage = "https://github.com/yuhuihui2011/VaSP"
	bioc = "VaSP" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/VaSP_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/VaSP/VaSP_1.14.0.tar.gz"]

    version("1.20.0", tag="RELEASE_3_21")
	version("1.14.0", sha256="de5d23ffd35c79a03de7f4c3c712aae69b1d49e26cdbad10618252c19b61b378")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ballgown", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
