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

	version("1.40.0", md5="cd3b9bb8a918c9497903f6274f323904")


