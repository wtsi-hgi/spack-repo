# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNndiagram(RPackage):
	"""Generator of 'LaTeX' Code for Drawing Neural Network Diagrams
with 'TikZ'

	Generates 'LaTeX' code for drawing well-formatted neural network diagrams with 'TikZ'. Users have to define number of neurons on each layer, and optionally define neuron connections they would like to keep or omit, layers they consider to be oversized and neurons they would like to draw with lighter color. They can also specify the title of diagram, color, opacity of figure, labels of layers, input and output neurons. In addition, this package helps to produce 'LaTeX' code for drawing activation functions which are crucial in neural network analysis. To make the code work in a 'LaTeX' editor, users need to install and import some 'TeX' packages including 'TikZ' in the setting of 'TeX' file.
	"""
	
	homepage = "https://github.com/ccfang2/nndiagram"
	cran = "nndiagram" 

	version("1.0.0", md5="5bd06c3bc4841fcbd051852b2c189e62")

	depends_on("r-dplyr", type=("build", "run"))
