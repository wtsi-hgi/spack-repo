# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSss(RPackage):
	"""Import Files in the Triple-s (Standard Survey Structure) Format

	Tools to import survey files in the '.sss' (triple-s) format. 
    The package provides the function 'read.sss()' that reads the '.asc' 
    (or '.csv') and '.sss' files of a triple-s survey data file. 
    See also <https://triple-s.org/>.
	"""
	
	homepage = "http://andrie.github.io/sss/"
	cran = "sss" 

	version("0.2.2", md5="460360963618a3670a74e436b04bb918")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
