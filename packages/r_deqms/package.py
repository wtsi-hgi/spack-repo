# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeqms(RPackage):
	"""a tool to perform statistical analysis of differential protein expression for quantitative proteomics data.

	DEqMS is developped on top of Limma. However, Limma assumes same prior variance for all genes. In proteomics, the accuracy of protein abundance estimates varies by the number of peptides/PSMs quantified in both label-free and labelled data. Proteins quantification by multiple peptides or PSMs are more accurate. DEqMS package is able to estimate different prior variances for proteins quantified by different number of PSMs/peptides, therefore acchieving better accuracy. The package can be applied to analyze both label-free and labelled proteomics data.
	"""
	
	bioc = "DEqMS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DEqMS_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DEqMS/DEqMS_1.20.0.tar.gz"]

	version("1.20.0", md5="bc308e6f683ca1bf0dcdb703274575ac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-limma@3.34:", type=("build", "run"))
