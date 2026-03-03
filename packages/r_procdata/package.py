# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProcdata(RPackage):
	"""Process Data Analysis

	Provides tools for exploratory process data analysis. Process data refers to the data describing
    participants' problem-solving processes in computer-based assessments. It is often recorded in computer
    log files. This package provides functions to read, process, and write process data. It also implements
    two feature extraction methods to compress the information stored in process data into standard 
    numerical vectors. This package also provides recurrent neural network based models that relate response processes 
    with other binary or scale variables of interest. The functions that involve training and evaluating neural networks 
    are wrappers of functions in 'keras'.
	"""
	
	cran = "ProcData" 

	version("0.3.2", md5="0c7b3cef07f48407d7016a4e3c91d72b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-keras@2.2.4:", type=("build", "run"))
	depends_on("python@2.7:", type=("build", "link", "run"))
	depends_on("py-tensorflow@1.13:", type=("build", "link", "run"))
