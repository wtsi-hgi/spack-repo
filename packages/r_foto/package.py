# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFoto(RPackage):
	"""Fourier Transform Textural Ordination

	A tool to use a principal component analysis on radially averaged
  two dimensional Fourier spectra to characterize image texture. The method
  within the context of ecology was first described by Couteron et al. (2005)
  <doi:10.1111/j.1365-2664.2005.01097.x> and expanded upon by
  Solorzano et al. (2018) <doi:10.1117/1.JRS.12.036006>
  using a moving window approach.
	"""
	
	homepage = "https://github.com/bluegreen-labs/foto"
	cran = "foto" 

	version("1.1", md5="0f1b8554c2c13d62830239c06bb64ba9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
