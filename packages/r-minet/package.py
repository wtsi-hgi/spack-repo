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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/minet_3.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/minet/minet_3.60.0.tar.gz"]

	version("3.66.0", tag="RELEASE_3_21")
	version("3.60.0", sha256="85470b4428fcd0f4f37db91efedb35274d3c03f5778cafdd07901ceed9e9629f")

	depends_on("r-infotheo", type=("build", "run"))
