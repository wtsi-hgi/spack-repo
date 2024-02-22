# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatriks(RPackage):
	"""Generates Raven-Like Matrices According to Rules

	Generates Raven like matrices according to different rules and the response list associated to the matrix. The package can generate matrices composed of 4 or 9 cells, along with a response list of 11 elements (the correct response + 10 incorrect responses). The matrices can be generated according to both logical rules (i.e., the relationships between the elements in the matrix are manipulated to create the matrix) and visual-spatial rules (i.e., the visual or spatial characteristics of the elements are manipulated to generate the matrix).
    The graphical elements of this package are based on the 'DescTools' package.
    This package has been developed within the PRIN2020 Project (Prot. 20209WKCLL) titled "Computerized, Adaptive and Personalized Assessment of Executive Functions and Fluid Intelligence" and founded by the Italian Ministry of Education and Research.
	"""
	
	cran = "matRiks" 

	version("0.1.3", md5="5565da7de795d595eddd6ae92fcff162")

	depends_on("r-desctools", type=("build", "run"))
