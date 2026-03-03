# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApercu(RPackage):
	"""Quick Look at your Data

	The goal is to print an "aperçu", a short view of a vector, a
    matrix, a data.frame, a list or an array. By default, it prints the first 5
    elements of each dimension. By default, the number of columns is equal to
    the number of lines. If you want to control the selection of the elements,
    you can pass a list, with each element being a vector giving the selection
    for each dimension.
	"""
	
	cran = "apercu" 

	version("0.2.5", md5="ff7fefe218203c5829c9b857f71011ca")
	version("0.2.4", md5="2e6c19dfc38fc680ba4af945cefae9af")

	depends_on("r-pls", type=("build", "run"))
