# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinet(RPackage):
	"""Mutual Information NETworks

	This package implements various algorithms for inferring mutual information networks from data.
	"""
	
	homepage = "http://minet.meyerp.com"
	bioc = "minet" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/minet_3.60.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/minet/minet_3.60.0.tar.gz"]

	version("3.60.0", md5="8aaab67519352be115568a301e98ef99")

	depends_on("r-infotheo", type=("build", "run"))
