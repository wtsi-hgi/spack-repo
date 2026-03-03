# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAntangiocool(RPackage):
	"""Anti-Angiogenic Peptide Prediction

	Machine learning based package to predict anti-angiogenic peptides using heterogeneous sequence descriptors. 'AntAngioCOOL' exploits five descriptor types of a peptide of interest to do prediction including: pseudo amino acid composition, k-mer composition, k-mer composition (reduced alphabet), physico-chemical profile and atomic profile. According to the obtained results, 'AntAngioCOOL' reached to a satisfactory performance in anti-angiogenic peptide prediction on a benchmark non-redundant independent test dataset.
	"""
	
	cran = "AntAngioCOOL" 

	version("1.2", md5="ca6fcff7645e71bd1a04ab387b5a3697")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-rweka", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
