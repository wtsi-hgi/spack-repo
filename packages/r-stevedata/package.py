# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStevedata(RPackage):
	"""Steve's Toy Data for Teaching About a Variety of Methodological,
Social, and Political Topics

	This is a collection of various kinds of data with broad uses for teaching. 
    My students, and academics like me who teach the same topics I teach, should find 
    this useful if their teaching workflow is also built around the R programming 
    language. The applications are multiple but mostly cluster on topics of statistical
    methodology, international relations, and political economy.
	"""
	
	homepage = "http://svmiller.com/stevedata/"
	cran = "stevedata" 

	version("1.1.0", md5="e5ab088990517955fddaf2018c346e93")

	depends_on("r@3.5:", type=("build", "run"))
