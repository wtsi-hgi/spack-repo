# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDirectional(RPackage):
	"""A Collection of Functions for Directional Data Analysis

	A collection of functions for directional data (including massive data, with millions of observations) analysis. Hypothesis testing, discriminant and regression analysis, MLE of distributions and more are included. The standard textbook for such data is the "Directional Statistics" by Mardia, K. V. and Jupp, P. E. (2000). Other references include a) Phillip J. Paine, Simon P. Preston Michail Tsagris and Andrew T. A. Wood (2018). "An elliptically symmetric angular Gaussian distribution". Statistics and Computing 28(3): 689-697. <doi:10.1007/s11222-017-9756-4>. b) Tsagris M. and Alenazi A. (2019). "Comparison of discriminant analysis methods on the sphere". Communications in Statistics: Case Studies, Data Analysis and Applications 5(4):467--491. <doi:10.1080/23737484.2019.1684854>. c) P. J. Paine, S. P. Preston, M. Tsagris and Andrew T. A. Wood (2020). "Spherical regression models with general covariates and anisotropic errors". Statistics and Computing 30(1): 153--165. <doi:10.1007/s11222-019-09872-2>. d) Tsagris M. and Alenazi A. (2024). "An investigation of hypothesis testing procedures for circular and spherical mean vectors". Communications in Statistics-Simulation and Computation, 53(3): 1387--1408. <doi:10.1080/03610918.2022.2045499>. e) Tsagris M. and Alzeley O. (2023). "Circular and spherical projected Cauchy distributions: A Novel Framework for Circular and Directional Data Modeling". <doi:10.48550/arXiv.2302.02468>. 
	"""
	
	cran = "Directional" 

	version("6.5", md5="1a42a66a0536fff8ebceb0450d9adfe3")
	version("6.4", md5="5107d99a866225b6b178e73f37520201")

	depends_on("r-bigstatsr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rfast2", type=("build", "run"))
	depends_on("r-rnanoflann", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
