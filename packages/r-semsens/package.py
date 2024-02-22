# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemsens(RPackage):
	"""A Tool for Sensitivity Analysis in Structural Equation Modeling

	Perform sensitivity analysis in structural equation modeling using 
    meta-heuristic optimization methods (e.g., ant colony optimization and others). 
    The references for the proposed methods are: 
    (1) Leite, W., & Shen, Z., Marcoulides, K., Fish, C., & Harring, J. (2022). 
    <doi:10.1080/10705511.2021.1881786>
    (2) Harring, J. R., McNeish, D. M., & Hancock, G. R. (2017)
    <doi:10.1080/10705511.2018.1506925>;
    (3) Fisk, C., Harring, J., Shen, Z., Leite, W., Suen, K., & Marcoulides, K. 
    (2022). <doi:10.1177/00131644211073121>;
    (4) Socha, K., & Dorigo, M. (2008) <doi:10.1016/j.ejor.2006.06.046>.
    We also thank Dr. Krzysztof Socha for sharing his research on ant colony optimization
    algorithm with continuous domains and associated R code,
    which provided the base for the development of this package.
	"""
	
	cran = "SEMsens" 

	version("1.5.5", md5="7bd194fcca739c3f43b98e625f9c3582")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
