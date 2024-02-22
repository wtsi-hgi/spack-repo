# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErr(RPackage):
	"""Customizable Object Sensitive Messages

	Messages should provide users with readable information 
    about R objects without flooding their console. 
    'cc()' concatenates vector and data frame values 
    into a grammatically correct string using commas, an ellipsis and conjunction. 
    'cn()' allows the user to define a string which varies based on a count.
    'co()' combines the two to produce a customizable object aware string.
    The package further facilitates this process by providing five 'sprintf'-like 
    types such as '%n' for the length of an object and '%o' for its name as
    well as wrappers for pasting objects and issuing errors, warnings and messages.
	"""
	
	homepage = "https://github.com/poissonconsulting/err"
	cran = "err" 

	version("0.2.0", md5="cfe916bb4f775dd2994e53517ea30158")

