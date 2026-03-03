# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REigenmodel(RPackage):
	"""Semiparametric Factor and Regression Models for Symmetric
Relational Data

	Estimation of the parameters in a model for
        symmetric relational data (e.g., the above-diagonal part of a
        square matrix), using a model-based eigenvalue decomposition
        and regression. Missing data is accommodated, and a posterior
        mean for missing data is calculated under the assumption that
        the data are missing at random. The marginal distribution of
        the relational data can be arbitrary, and is fit with an
        ordered probit specification. See Hoff (2007) <arXiv:0711.1146> 
        for details on the model.  
	"""
	
	homepage = "https://pdhoff.github.io/"
	cran = "eigenmodel" 

	version("1.11", md5="530e52dd3cad43259c438c6c1d4397d1")

