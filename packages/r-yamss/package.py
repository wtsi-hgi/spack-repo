# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYamss(RPackage):
	"""Tools for high-throughput metabolomics

	Tools to analyze and visualize high-throughput metabolomics data aquired using chromatography-mass spectrometry. These tools preprocess data in a way that enables reliable and powerful differential analysis.
	"""
	
	homepage = "https://github.com/hansenlab/yamss"
	bioc = "yamss" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/yamss_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/yamss/yamss_1.28.0.tar.gz"]

    version("1.34.1", tag="RELEASE_3_21")
	version("1.28.0", sha256="cbf7f1b175b8d5d6514419f2f0f4ccef57f10f3d32b92bc4e8acf9cacbf02d9b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics@0.15.3:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mzr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
