# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopdownrdata(RPackage):
	"""Example Files for the topdownr R Package

	Example data for the topdownr package generated on a Thermo Orbitrap Fusion Lumos MS device.
	"""
	
	homepage = "https://github.com/sgibb/topdownrdata/"
	bioc = "topdownrdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/topdownrdata_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/topdownrdata/topdownrdata_1.24.0.tar.gz"]

	version("1.24.0", md5="28e746b858956bea0967344bfe363e7d")

	depends_on("r-topdownr", type=("build", "run"))

