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

    version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="22a5321300a668ac67bb395ba6df963e078e82fe0b981f8e2a56f983306f9d07")

	depends_on("r-topdownr", type=("build", "run"))

