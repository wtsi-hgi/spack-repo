# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdynmc(RPackage):
	"""Moment Condition Based Estimation of Linear Dynamic Panel Data
Models

	Linear dynamic panel data modeling based on linear and
    nonlinear moment conditions as proposed by
    Holtz-Eakin, Newey, and Rosen (1988) <doi:10.2307/1913103>,
    Ahn and Schmidt (1995) <doi:10.1016/0304-4076(94)01641-C>,
    and Arellano and Bover (1995) <doi:10.1016/0304-4076(94)01642-D>.
    Estimation of the model parameters relies on the Generalized
    Method of Moments (GMM), numerical optimization (when nonlinear
    moment conditions are employed) and the computation of closed
    form solutions (when estimation is based on linear moment
    conditions). One-step, two-step and iterated estimation is
    available. For inference and specification
    testing, Windmeijer (2005) <doi:10.1016/j.jeconom.2004.02.005>
    and doubly corrected standard errors
    (Hwang, Kang, Lee, 2021 <doi:10.1016/j.jeconom.2020.09.010>)
    are available. Additionally, serial correlation tests, tests for
    overidentification, and Wald tests are provided. Functions for
    visualizing panel data structures and modeling results obtained
    from GMM estimation are also available. The plot methods include
    functions to plot unbalanced panel structure, coefficient ranges
    and coefficient paths across GMM iterations (the latter is
    implemented according to the plot shown in
    Hansen and Lee, 2021 <doi:10.3982/ECTA16274>).
    For a more detailed description of the functionality, please
    see Fritsch, Pua, Schnurbus (2021) <doi:10.32614/RJ-2021-035>.
	"""
	
	homepage = "https://github.com/markusfritsch/pdynmc"
	cran = "pdynmc" 

	version("0.9.10", md5="788646c107852a1569601b5ecf6d05dd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table@1.12.2:", type=("build", "run"))
	depends_on("r-mass@7.3.51.4:", type=("build", "run"))
	depends_on("r-matrix@1.2.17:", type=("build", "run"))
	depends_on("r-optimx@2018.07.10:", type=("build", "run"))
	depends_on("r-rdpack@0.11.0:", type=("build", "run"))
