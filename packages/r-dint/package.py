# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDint(RPackage):
	"""A Toolkit for Year-Quarter, Year-Month and Year-Isoweek Dates

	S3 classes and methods to create and work
    with year-quarter, year-month and year-isoweek vectors. Basic
    arithmetic operations (such as adding and subtracting) are supported,
    as well as formatting and converting to and from standard R date
    types.
	"""
	
	homepage = "https://github.com/s-fleck/dint"
	cran = "dint" 

	version("2.1.4", md5="3df214d8619c6a85d311c0a46399a838")

