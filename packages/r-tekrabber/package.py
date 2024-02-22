# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTekrabber(RPackage):
	"""An R package estimates the correlations of orthologs and transposable elements between two species

	TEKRABber is made to provide a user-friendly pipeline for comparing orthologs and transposable elements (TEs) between two species. It considers the orthology confidence between two species from BioMart to normalize expression counts and detect differentially expressed orthologs/TEs. Then it provides one to one correlation analysis for desired orthologs and TEs. There is also an app function to have a first insight on the result. Users can prepare orthologs/TEs RNA-seq expression data by their own preference to run TEKRABber following the data structure mentioned in the vignettes.
	"""
	
	homepage = "https://github.com/ferygood/TEKRABber"
	bioc = "TEKRABber" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/TEKRABber_1.6.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/TEKRABber/TEKRABber_1.6.0.tar.gz"]

	version("1.6.0", md5="145026d8a5e02ec94f8a2a1f5405851e")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-apeglm", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-scbn", type=("build", "run"))
