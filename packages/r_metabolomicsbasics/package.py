# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabolomicsbasics(RPackage):
	"""Basic Functions to Investigate Metabolomics Data Matrices

	A set of functions to investigate raw data from (metabol)omics experiments intended to be used on a raw data matrix, i.e. following peak picking and signal deconvolution. Functions can be used to normalize data, detect biomarkers and perform sample classification. A detailed description of best practice usage may be found in the publication <doi:10.1007/978-1-4939-7819-9_20>.
	"""
	
	homepage = "https://github.com/janlisec/MetabolomicsBasics"
	cran = "MetabolomicsBasics" 

	version("1.4.5", md5="247cbfbd7bdc26db48a5c76fd698cf82")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-c50", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-interpretmsspectrum", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-webchem", type=("build", "run"))
