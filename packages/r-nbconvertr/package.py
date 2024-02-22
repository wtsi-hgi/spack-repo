# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbconvertr(RPackage):
	"""Vignette Engine Wrapping Jupyter Notebooks

	
  Calls the 'Jupyter' script 'nbconvert' to create vignettes from
  notebooks. Those notebooks ('.ipynb' files) are files containing rich text,
  code, and its output. Code cells can be edited and evaluated interactively.
  See <https://jupyter.org/> for more information.
	"""
	
	cran = "nbconvertR" 

	version("1.3.2", md5="05d104a573a069626f3e98db24ce88ce")

	depends_on("pandoc", type=("build", "link", "run"))
	depends_on("py-jupyter", type=("build", "link", "run"))
	depends_on("py-nbconvert", type=("build", "link", "run"))
