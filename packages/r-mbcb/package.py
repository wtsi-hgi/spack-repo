# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbcb(RPackage):
	"""MBCB (Model-based Background Correction for Beadarray)

	This package provides a model-based background correction method, which incorporates the negative control beads to pre-process Illumina BeadArray data.
	"""
	
	homepage = "http://www.utsouthwestern.edu"
	bioc = "MBCB"

	version("1.62.0", commit="9d2f26b5793c8416caa86788e289044d0b41619b")
	version("1.56.0", commit="056b1dd08e990797b50eb29658df4b6c10095f45")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
