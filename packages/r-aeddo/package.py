# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAeddo(RPackage):
	"""Automated and Early Detection of Disease Outbreaks

	A powerful tool for automating the early detection of disease
             outbreaks in time series data. 'aeddo' employs advanced statistical 
             methods, including hierarchical models, in an innovative manner to 
             effectively characterize outbreak signals. It is particularly useful 
             for epidemiologists, public health professionals, and researchers 
             seeking to identify and respond to disease outbreaks in a timely 
             fashion. For a detailed reference on hierarchical models, consult 
             Henrik Madsen and Poul Thyregod's book (2011), ISBN: 9781420091557.
	"""
	
	homepage = "https://ssi-dk.github.io/aeddo/"
	cran = "aeddo" 

	version("0.1.1", md5="832e63b24d33c4be8a36d029b15282f7")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
