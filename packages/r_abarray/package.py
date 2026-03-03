# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbarray(RPackage):
	"""Microarray QA and statistical data analysis for Applied Biosystems Genome Survey Microrarray (AB1700) gene expression data.

	Automated pipline to perform gene expression analysis for Applied Biosystems Genome Survey Microarray (AB1700) data format. Functions include data preprocessing, filtering, control probe analysis, statistical analysis in one single function. A GUI interface is also provided. The raw data, processed data, graphics output and statistical results are organized into folders according to the analysis settings used.
	"""
	
	bioc = "ABarray" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ABarray_1.70.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ABarray/ABarray_1.70.0.tar.gz"]

	version("1.70.0", md5="59e686f9daf6990fbe6e1594b8676197")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
