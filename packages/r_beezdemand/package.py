# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeezdemand(RPackage):
	"""Behavioral Economic Easy Demand

	Facilitates many of the analyses performed in studies of
    behavioral economic demand. The package supports commonly-used options for
		modeling operant demand including (1) data screening proposed by Stein,
		Koffarnus, Snider, Quisenberry, & Bickel (2015; <doi:10.1037/pha0000020>),
		(2) fitting models of demand such as linear (Hursh, Raslear, Bauman,
		& Black, 1989, <doi:10.1007/978-94-009-2470-3_22>), exponential	(Hursh & Silberberg, 2008,
		<doi:10.1037/0033-295X.115.1.186>) and modified exponential (Koffarnus,
		Franck, Stein, & Bickel, 2015, <doi:10.1037/pha0000045>), and (3) calculating
		numerous measures	relevant to applied behavioral economists (Intensity,
		Pmax, Omax). Also	supports plotting and comparing data.
	"""
	
	homepage = "https://github.com/brentkaplan/beezdemand"
	cran = "beezdemand" 

	version("0.1.2", md5="4e03a3112fcd51175402ccb94253f236")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-nlsr", type=("build", "run"))
	depends_on("r-nlstools", type=("build", "run"))
	depends_on("r-nls2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
