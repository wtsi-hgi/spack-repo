# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmen(RPackage):
	"""Additive and Multiplicative Effects Models for Networks and
Relational Data

	Analysis of dyadic network and relational data using additive and
    multiplicative effects (AME) models. The basic model includes
    regression terms, the covariance structure of the social relations model
    (Warner, Kenny and Stoto (1979) <DOI:10.1037/0022-3514.37.10.1742>, 
    Wong (1982) <DOI:10.2307/2287296>), and multiplicative factor
    models (Hoff(2009) <DOI:10.1007/s10588-008-9040-4>). 
    Several different link functions accommodate different
    relational data structures, including binary/network data, normal
    relational data, zero-inflated positive outcomes using a tobit model, ordinal relational data and data from
    fixed-rank nomination schemes. Several of these link functions are
    discussed in Hoff, Fosdick, Volfovsky and Stovel (2013) 
    <DOI:10.1017/nws.2013.17>. Development of this
    software was supported in part by NIH grant R01HD067509.
	"""
	
	homepage = "https://github.com/pdhoff/amen"
	cran = "amen" 

	version("1.4.5", md5="8a656884af120bb00b06e2eec84faf62")

	depends_on("r@3.5:", type=("build", "run"))
