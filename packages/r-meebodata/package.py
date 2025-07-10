# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeebodata(RPackage):
	"""MEEBO set and MEEBO controls.

	R objects describing the MEEBO set.
	"""
	
	homepage = "http://alizadehlab.stanford.edu/"
	bioc = "MEEBOdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/MEEBOdata_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/MEEBOdata/MEEBOdata_1.40.0.tar.gz"]

	version("1.40.0", sha256="67a8e144fc8c0d684a2b5f84a8511801df7d8710dfae272d1a15022b2d12295a")


