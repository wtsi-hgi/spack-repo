# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSicegar(RPackage):
	"""Analysis of Single-Cell Viral Growth Curves

	
    Aims to quantify time intensity data by using sigmoidal and
    double sigmoidal curves. It fits straight lines, sigmoidal, 
    and double sigmoidal curves on to time vs intensity data. 
    Then all the fits are used to make decision on which model 
    best describes the data. This method was first developed 
    in the context of single-cell viral growth analysis (for
    details, see Caglar et al. (2018) <doi:10.7717/peerj.4251>),
    and the package name stands for "SIngle CEll Growth Analysis in R".
	"""
	
	homepage = "https://github.com/wilkelab/sicegar"
	cran = "sicegar" 

	version("0.2.4", md5="a26c502aa7489a0a3365ccc2150b36f0")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
