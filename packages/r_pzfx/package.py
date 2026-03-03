# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPzfx(RPackage):
	"""Read and Write 'GraphPad Prism' Files

	Read and write 'GraphPad Prism' '.pzfx' files in R.
	"""
	
	homepage = "https://github.com/Yue-Jiang/pzfx"
	cran = "pzfx" 

	version("0.3.0", md5="6768dd28b738772bfcf03a5d2a7b6cc3")

	depends_on("r-xml2@1.2:", type=("build", "run"))
