# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeomodels(RPackage):
	"""Procedures for Gaussian and Non Gaussian Geostatistical (Large)
Data Analysis

	Functions for Gaussian and Non Gaussian (bivariate) spatial and spatio-temporal data analysis are provided for a) simulation and inference  for random fields using standard likelihood and a likelihood approximation  method called  weighted composite likelihood based on pairs and b) prediction using (local) best linear unbiased prediction. Weighted composite likelihood can be very efficient for estimating massive datasets. Both regression and spatial (temporal) dependence analysis can be jointly performed. Covariance functions for spatial and spatial-temporal data on Euclidean domains and spheres are provided. There are also many useful functions for plotting and performing diagnostic analysis. Different non Gaussian random fields can be considered in the analysis. Among them, random fields with marginal distributions such as Skew-Gaussian, Student-t, Tukey-h, Sin-Arcsin, Two-piece, Weibull, Gamma, Log-Gaussian, Binomial, Negative Binomial  and Poisson. See the URL for the papers associated with this package, as for instance, Bevilacqua and Gaetan (2015) <doi:10.1007/s11222-014-9460-6>, Bevilacqua et al. (2016) <doi:10.1007/s13253-016-0256-3>, Vallejos et al. (2020) <doi:10.1007/978-3-030-56681-4>, Bevilacqua et. al (2020) <doi:10.1002/env.2632>, Bevilacqua et. al (2021) <doi:10.1111/sjos.12447>, Bevilacqua et al. (2022) <doi:10.1016/j.jmva.2022.104949>, Morales-Navarrete et al. (2023) <doi:10.1080/01621459.2022.2140053>, and a large class of examples and tutorials.
	"""
	
	homepage = "https://vmoprojs.github.io/GeoModels-page/"
	cran = "GeoModels" 

	version("1.1.9", md5="3ac53cad4a25678490c0080a1c0de47b")
	version("1.1.7", md5="5eaeb2a961208ec4d518233b142dae99")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-gpvecchia", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-mapproj", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-dfoptim", type=("build", "run"))
	depends_on("r-dotcall64", type=("build", "run"))
	depends_on("r-optimparallel", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-pbivnorm", type=("build", "run"))
	depends_on("r-zipfr", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-nabor", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-hypergeo", type=("build", "run"))
	depends_on("r-lamw", type=("build", "run"))
	depends_on("r-gpgp", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
