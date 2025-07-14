# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaa(RPackage):
	"""PAA (Protein Array Analyzer)

	PAA imports single color (protein) microarray data that has been saved in gpr file format - esp. ProtoArray data. After preprocessing (background correction, batch filtering, normalization) univariate feature preselection is performed (e.g., using the "minimum M statistic" approach - hereinafter referred to as "mMs"). Subsequently, a multivariate feature selection is conducted to discover biomarker candidates. Therefore, either a frequency-based backwards elimination aproach or ensemble feature selection can be used. PAA provides a complete toolbox of analysis tools including several different plots for results examination and evaluation.
	"""
	
	homepage = "http://www.ruhr-uni-bochum.de/mpc/software/PAA/"
	bioc = "PAA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PAA_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PAA/PAA_1.36.0.tar.gz"]

	version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="a2000b7af80f2550756668074c8ebd503bb423d9f94f5a69b8e802c3ef9bdb49")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mrmre", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
