# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLineartestr(RPackage):
	"""Linear Specification Testing

	Tests whether the linear hypothesis of a model
    is correct specified using Dominguez-Lobato test. Also Ramsey's RESET (Regression Equation 
    Specification Error Test) test is implemented and Wald tests can be carried out. 
    Although RESET test is widely used to 
    test the linear hypothesis of a model, Dominguez and Lobato (2019) proposed a novel 
    approach that generalizes well known specification tests such as Ramsey's. This test 
    relies on wild-bootstrap; this package implements this approach to be 
    usable with any function that fits linear models and is compatible with 
    the update() function such as 'stats'::lm(), 'lfe'::felm() and 'forecast'::Arima(), 
    for ARMA (autoregressive–moving-average) models. 
    Also the package can handle custom statistics such as Cramer von Mises and Kolmogorov 
    Smirnov, described by the authors, and custom distributions such as Mammen (discrete 
    and continuous) and Rademacher.
    Manuel A. Dominguez & Ignacio N. Lobato (2019) <doi:10.1080/07474938.2019.1687116>.
	"""
	
	homepage = "https://github.com/FedericoGarza/lineartestr"
	cran = "lineartestr" 

	version("1.0.0", md5="d8c2778048c2b34c124db7ddd0f0cf5d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
