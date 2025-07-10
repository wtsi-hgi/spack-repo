# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClippda(RPackage):
	"""A package for the clinical proteomic profiling data analysis

	Methods for the nalysis of data from clinical proteomic profiling studies. The focus is on the studies of human subjects, which are often observational case-control by design and have technical replicates. A method for sample size determination for planning these studies is proposed. It incorporates routines for adjusting for the expected heterogeneities and imbalances in the data and the within-sample replicate correlations.
	"""
	
	homepage = "http://www.cancerstudies.bham.ac.uk/crctu/CLIPPDA.shtml"
	bioc = "clippda" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/clippda_1.52.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/clippda/clippda_1.52.0.tar.gz"]

	version("1.52.0", sha256="8fab641f40a4e8d5187c6a5fe0ae800b5f33379bb2ee8f01647efb78b5aefd86")

	depends_on("r@2.13.1:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
