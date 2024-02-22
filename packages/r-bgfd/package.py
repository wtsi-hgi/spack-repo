# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgfd(RPackage):
	"""Bell-G and Complementary Bell-G Family of Distributions

	Evaluates the probability density function, cumulative distribution function, quantile function, random numbers, survival function, hazard rate function, and maximum likelihood estimates for the following distributions: Bell exponential, Bell extended exponential, Bell Weibull, Bell extended Weibull, Bell-Fisk, Bell-Lomax, Bell Burr-XII, Bell Burr-X, complementary Bell exponential, complementary Bell extended exponential, complementary Bell Weibull, complementary Bell extended Weibull, complementary Bell-Fisk, complementary Bell-Lomax, complementary Bell Burr-XII and complementary Bell Burr-X distribution. Related work includes:
     a) Fayomi A., Tahir M. H., Algarni A., Imran M. and Jamal F. (2022). "A new useful exponential model with applications to quality control and 
        actuarial data". Computational Intelligence and Neuroscience, 2022. <doi:10.1155/2022/2489998>.
     b) Alanzi, A. R., Imran M., Tahir M. H., Chesneau C., Jamal F. Shakoor S. and Sami, W. (2023). "Simulation analysis, 
        properties and applications on a new Burr XII model based on the Bell-X functionalities". AIMS Mathematics, 8(3): 6970-7004. <doi:10.3934/math.2023352>.
     c) Algarni A. (2022). "Group Acceptance Sampling Plan Based on New Compounded Three-Parameter Weibull Model". Axioms, 11(9): 438. <doi:10.3390/axioms11090438>.
	"""
	
	cran = "BGFD" 

	version("0.1", md5="3f3cbb70d3106774909fe69a62a6bf99")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-adequacymodel", type=("build", "run"))
