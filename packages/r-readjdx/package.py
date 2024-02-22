# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadjdx(RPackage):
	"""Import Data in the JCAMP-DX Format

	Import data written in the JCAMP-DX format. This is an instrument-independent format used in the field of spectroscopy. Examples include IR, NMR, and Raman spectroscopy. See the vignette for background and supported formats.  The official JCAMP-DX site is <http://www.jcamp-dx.org/>.
	"""
	
	homepage = "https://github.com/bryanhanson/readJDX"
	cran = "readJDX" 

	version("0.6.4", md5="e653fb13a8bd68521c6679374fa16bdc")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
