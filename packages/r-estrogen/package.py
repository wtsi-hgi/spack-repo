# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REstrogen(RPackage):
	"""Microarray dataset that can be used as example for 2x2 factorial designs

	Data from 8 Affymetrix genechips, looking at a 2x2 factorial design (with 2 repeats per level).
	"""
	
	bioc = "estrogen" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/estrogen_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/estrogen/estrogen_1.48.0.tar.gz"]

	version("1.48.0", sha256="95aef9a936e8673bda5cb5d829d17b826046c2161f4efb5f571def236f787e59")


