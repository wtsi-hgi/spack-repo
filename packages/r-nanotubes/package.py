# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNanotubes(RPackage):
	"""Mouse nanotube CAGE data

	Cap Analysis of Gene Expression (CAGE) data from "Identification of Gene Transcription Start Sites and Enhancers Responding to Pulmonary Carbon Nanotube Exposure in Vivo" by Bornholdt et al. supplied as CAGE Transcription Start Sites (CTSSs).
	"""
	
	homepage = "https://github.com/MalteThodberg/nanotubes"
	bioc = "nanotubes" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/nanotubes_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/nanotubes/nanotubes_1.18.0.tar.gz"]

	version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="caab16942bfb50e9c0e48c2589a83a4abc4766a73841e34da2d7cc1a0af0072a")

	depends_on("r@3.6:", type=("build", "run"))

