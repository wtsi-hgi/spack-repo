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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MBCB_1.56.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MBCB/MBCB_1.56.0.tar.gz"]

    version("1.62.0", tag="RELEASE_3_21")
	version("1.56.0", sha256="fd1e5b3f7bdd1deabfbf858ab7fbd9cc7115dee72c1f00777fdcfa99cfa35ec2")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
