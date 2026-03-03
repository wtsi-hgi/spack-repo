# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedtools(RPackage):
	"""Creating and Working with Pedigrees and Marker Data

	A comprehensive collection of tools for creating,
    manipulating and visualising pedigrees and genetic marker data.
    Pedigrees can be read from text files or created on the fly with
    built-in functions. A range of utilities enable modifications like
    adding or removing individuals, breaking loops, and merging pedigrees.
    An online tool for creating pedigrees interactively, based on
    'pedtools', is available at <https://magnusdv.shinyapps.io/quickped>.
    'pedtools' is the hub of the 'pedsuite', a collection of packages for
    pedigree analysis. A detailed presentation of the 'pedsuite' is given
    in the book 'Pedigree Analysis in R' (Vigeland, 2021,
    ISBN:9780128244302).
	"""
	
	homepage = "https://github.com/magnusdv/pedtools"
	cran = "pedtools" 

	version("2.6.0", md5="b131e72d011ba340804b27e808f94edd")
	version("2.5.0", md5="4deae6c59019082b8035e4dc314517bc")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-kinship2", type=("build", "run"))
	depends_on("r-pedmut", type=("build", "run"))
