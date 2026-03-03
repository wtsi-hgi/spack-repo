# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROoplah(RPackage):
	"""Helper Functions for Class Object-Oriented Programming

	Helper functions for coding object-oriented programming with
    a focus on R6. Includes functions for assertions and testing, looping,
    and re-usable design patterns including Abstract and Decorator
    classes.
	"""
	
	homepage = "https://xoopR.github.io/ooplah/"
	cran = "ooplah" 

	version("0.2.0", md5="8d3cbd36f5c17c6078b53dda13a1a402")

	depends_on("r-r6", type=("build", "run"))
