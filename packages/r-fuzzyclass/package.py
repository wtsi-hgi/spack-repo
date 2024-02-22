# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzyclass(RPackage):
	"""Fuzzy and Non-Fuzzy Classifiers

	It provides classifiers which can be used for discrete variables and for continuous variables based on the Naive Bayes and Fuzzy Naive Bayes hypothesis. Those methods were developed by researchers belong to the 'Laboratory of Technologies for Virtual Teaching and Statistics (LabTEVE)' and 'Laboratory of Applied Statistics to Image Processing and Geoprocessing (LEAPIG)' at 'Federal University of Paraiba, Brazil'. They considered some statistical distributions and their papers were published in the scientific literature, as for instance, the Gaussian classifier using fuzzy parameters, proposed by 'Moraes, Ferreira and Machado' (2021) <doi:10.1007/s40815-020-00936-4>.
	"""
	
	homepage = "https://github.com/leapigufpb/FuzzyClass"
	cran = "FuzzyClass" 

	version("0.1.6", md5="d25532884a1022df42eca358bbf35ff7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-trapezoid", type=("build", "run"))
