# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBazar(RPackage):
	"""Miscellaneous Basic Functions

	A collection of miscellaneous functions for 
    copying objects to the clipboard ('Copy');
    manipulating strings ('concat', 'mgsub', 'trim', 'verlan'); 
    loading or showing packages ('library_with_dep', 'require_with_dep', 
    'sessionPackages'); 
    creating or testing for named lists ('nlist', 'as.nlist', 'is.nlist'), 
    formulas ('is.formula'), empty objects ('as.empty', 'is.empty'), 
    whole numbers ('as.wholenumber', 'is.wholenumber'); 
    testing for equality ('almost.equal', 'almost.zero') and computing 
    uniqueness ('almost.unique'); 
    getting modified versions of usual functions ('rle2', 'sumNA'); 
    making a pause or a stop ('pause', 'stopif'); 
    converting into a function ('as.fun'); 
    providing a C like ternary operator ('condition %?% true %:% false'); 
    finding packages and functions ('get_all_pkgs', 'get_all_funs');
    and others ('erase', '%nin%', 'unwhich', 'top', 'bot', 'normalize'). 
	"""
	
	homepage = "https://github.com/paulponcet/bazar"
	cran = "bazar" 

	version("1.0.11", md5="c48980ea6232edb9af3f91276c10c8ec")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-kimisc", type=("build", "run"))
