# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDauphin(RPackage):
	"""Compact Standard for Australian Phone Numbers

	Phone numbers are often represented as strings because there
    is no obvious and suitable native representation for them.  This leads
    to high memory use and a lack of standard representation.  The package
    provides integer representation of Australian phone numbers with optional
    raw vector calling code. The package name is an extension of 'au' and 'ph'.
	"""
	
	cran = "dauphin" 

	version("0.3.1", md5="de3069c5c682e2df0ad49b1c43159570")

