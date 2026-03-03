# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFresaCad(RPackage):
	"""Feature Selection Algorithms for Computer Aided Diagnosis

	Contains a set of utilities for building and testing statistical models (linear, logistic,ordinal or COX) for Computer Aided Diagnosis/Prognosis applications. Utilities include data adjustment, univariate analysis, model building, model-validation, longitudinal analysis, reporting and visualization.
	"""
	
	cran = "FRESA.CAD" 

	version("3.4.7", md5="497ce1a469a34baa1eac3683bf996f9c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-misctools", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
