# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelectionIndex(RPackage):
	"""Analysis of Selection Index in Plant Breeding

	The aim of most plant breeding programmes is simultaneous improvement of several characters. An objective method involving simultaneous selection for several attributes then becomes necessary. It has been recognised that most rapid improvements in the economic value is expected from selection applied simultaneously to all the characters which determine the economic value of a plant, and appropriate assigned weights to each character according to their economic importance, heritability and correlations between characters. So the selection for economic value is a complex matter. If the component characters are combined together into an index in such a way that when selection is applied to the index, as if index is the character to be improved, most rapid improvement of economic value is expected. Such an index was first proposed by Smith (1937 <doi:10.1111/j.1469-1809.1936.tb02143.x>) based on the Fisher's (1936 <doi:10.1111/j.1469-1809.1936.tb02137.x>) "discriminant function" Dabholkar (1999 <https://books.google.co.in/books?id=mlFtumAXQ0oC&lpg=PA4&ots=Xgxp1qLuxS&dq=elements%20of%20biometrical%20genetics&lr&pg=PP1#v=onepage&q&f=false>). In this package selection index is calculated based on the Smith (1937) selection index method.
	"""
	
	homepage = "https://github.com/zankrut20/selection.index"
	cran = "selection.index" 

	version("1.2.0", md5="898b6fe190aaa2b37027d8b805d3034a")

	depends_on("r@2.10:", type=("build", "run"))
