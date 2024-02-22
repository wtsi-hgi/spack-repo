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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MBCB_1.56.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MBCB/MBCB_1.56.0.tar.gz"]

	version("1.56.0", md5="51a88491b8d5872a1088def3f6113466")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
