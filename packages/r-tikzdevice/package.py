# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTikzdevice(RPackage):
	"""R Graphics Output in LaTeX Format

	Provides a graphics output device for R that records plots
        in a LaTeX-friendly format. The device transforms plotting
        commands issued by R functions into LaTeX code blocks. When
        included in a LaTeX document, these blocks are interpreted with
        the help of 'TikZ'---a graphics package for TeX and friends
        written by Till Tantau. Using the 'tikzDevice', the text of R
        plots can contain LaTeX commands such as mathematical formula.
        The device also allows arbitrary LaTeX code to be inserted into
        the output stream.
	"""
	
	homepage = "https://github.com/daqana/tikzDevice"
	cran = "tikzDevice" 

	version("0.12.6", md5="794e8ce86c5fe333ded64a41b4a8e508")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-filehash@2.3:", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
