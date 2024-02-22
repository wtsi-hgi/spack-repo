# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeeppincs(RPackage):
	"""Protein Interactions and Networks with Compounds based on Sequences using Deep Learning

	The identification of novel compound-protein interaction (CPI) is important in drug discovery. Revealing unknown compound-protein interactions is useful to design a new drug for a target protein by screening candidate compounds. The accurate CPI prediction assists in effective drug discovery process. To identify potential CPI effectively, prediction methods based on machine learning and deep learning have been developed. Data for sequences are provided as discrete symbolic data. In the data, compounds are represented as SMILES (simplified molecular-input line-entry system) strings and proteins are sequences in which the characters are amino acids. The outcome is defined as a variable that indicates how strong two molecules interact with each other or whether there is an interaction between them. In this package, a deep-learning based model that takes only sequence information of both compounds and proteins as input and the outcome as output is used to predict CPI. The model is implemented by using compound and protein encoders with useful features. The CPI model also supports other modeling tasks, including protein-protein interaction (PPI), chemical-chemical interaction (CCI), or single compounds and proteins. Although the model is designed for proteins, DNA and RNA can be used if they are represented as sequences.
	"""
	
	bioc = "DeepPINCS" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DeepPINCS_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DeepPINCS/DeepPINCS_1.10.0.tar.gz"]

	version("1.10.0", md5="cc5fbdd874a89f88ffed9c215f1e3d74")

	depends_on("r-keras", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-catencoders", type=("build", "run"))
	depends_on("r-matlab", type=("build", "run"))
	depends_on("r-rcdk", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-tokenizers", type=("build", "run"))
	depends_on("r-webchem", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ttgsea", type=("build", "run"))
	depends_on("r-prroc", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
