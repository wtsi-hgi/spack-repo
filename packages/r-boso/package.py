# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoso(RPackage):
	"""Bilevel Optimization Selector Operator

	A novel feature selection algorithm for linear regression called 
    BOSO (Bilevel Optimization Selector Operator). The main contribution is the 
    use a bilevel optimization problem to select the variables in the training 
    problem that minimize the error in the validation set. Preprint available: 
    [Valcarcel, L. V., San Jose-Eneriz, E., Cendoya, X., Rubio, A., Agirre, X., 
    Prosper, F., & Planes, F. J. (2020). "BOSO: a novel feature selection 
    algorithm for linear regression with high-dimensional data." bioRxiv. 
    <doi:10.1101/2020.11.18.388579>]. 
    In order to run the vignette, it is recommended to install the 'bestsubset' package,
    using the following command: devtools::install_github(repo="ryantibs/best-subset", subdir="bestsubset").
    If you do not have gurobi, run devtools::install_github(repo="lvalcarcel/best-subset", subdir="bestsubset").
	"""
	
	cran = "BOSO" 

	version("1.0.3", md5="9bf56020684594d2b9e2de57982e055d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
